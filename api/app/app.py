"""
Módulo principal de la aplicación FastAPI.

Configura la instancia de la aplicación, registra los routers,
middleware y manejo de excepciones globales.
"""
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import router_productos, router_categorias
from app.infrastructure.database import init_db
from app.domain.exceptions import (
    ProductNotFoundError,
    ProductAlreadyExistsError,
    InvalidProductDataError,
    DatabaseError
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestiona el ciclo de vida de la aplicación."""
    await init_db()
    yield


app = FastAPI(
    title="API de Gestión de Productos",
    description="API REST para la gestión de productos con operaciones CRUD",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ProductNotFoundError)
async def product_not_found_handler(request: Request, exc: ProductNotFoundError):
    """Maneja errores de producto no encontrado."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "Producto no encontrado",
            "detail": f"El producto con ID {exc.product_id} no existe"
        }
    )


@app.exception_handler(ProductAlreadyExistsError)
async def product_already_exists_handler(request: Request, exc: ProductAlreadyExistsError):
    """Maneja errores de producto duplicado."""
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "Producto duplicado",
            "detail": f"Ya existe un producto con el nombre '{exc.name}'"
        }
    )


@app.exception_handler(InvalidProductDataError)
async def invalid_product_data_handler(request: Request, exc: InvalidProductDataError):
    """Maneja errores de datos inválidos."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Datos inválidos",
            "detail": exc.message
        }
    )


@app.exception_handler(DatabaseError)
async def database_error_handler(request: Request, exc: DatabaseError):
    """Maneja errores de base de datos."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Error de base de datos",
            "detail": "Ha ocurrido un error al procesar la solicitud"
        }
    )


app.include_router(router_productos, prefix="/products", tags=["Productos"])
app.include_router(router_categorias, prefix="/categories", tags=["Categorías"])


@app.get("/", tags=["Raíz"])
async def root():
    """Endpoint raíz que muestra información de la API."""
    return {
        "message": "API de Gestión de Productos",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health", tags=["Salud"])
async def health_check():
    """Endpoint de verificación de estado de la aplicación."""
    return {
        "status": "healthy",
        "service": "product-api"
    }


if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "false").lower() == "true"
    
    uvicorn.run(
        "app.app:app",
        host=host,
        port=port,
        reload=reload
    )