# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener el proyecto completo y arrancable. Guarda los archivos que te devuelva en la
carpeta del repo, respetando exactamente las rutas.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `api/app/api/routers.py` — La fase "Definición del modelo de producto" se implementa aqui: este archivo es el ejercicio.
- `api/app/application/services.py` — La fase "Implementación de endpoints CRUD" se implementa aqui: este archivo es el ejercicio.
- `api/app/infrastructure/database.py` — La fase "Definición del modelo de producto" ya venia resuelta por el codigo base: este archivo pasa a ser el ejercicio.

## Mapa de componentes

El repo tiene una carpeta por componente. Cada uno se instala y verifica dentro de la suya.

| Componente | Carpeta | Rol | Capa | Track | Tecnologias |
|---|---|---|---|---|---|
| `api` | `api/` | practice | server | Python | Amazon API Gateway |
| `data` | `data/` | chapter, support | data | Ingeniero de datos | - |

## Orden de arranque

1. `cd api && pip install -r requirements.txt && python -m compileall -q app && python -c "import app"` — componente `api` (practice).
2. `cd data && pip install -e . && python src/main.py` — componente `data` (chapter, support).

### Contratos entre componentes

- `api` expone http (api: http://localhost:8000):
  - `POST /products`
  - `GET /products/{product_id}`
  - `PUT /products/{product_id}`
  - `DELETE /products/{product_id}`
  - `GET /products`

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **api/app/__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `api/app/infrastructure/repositories.py` — `ProductCreate.model_dump`: Se invoca `model_dump` sobre `ProductCreate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `api/app/infrastructure/repositories.py` — `ProductUpdate.model_dump`: Se invoca `model_dump` sobre `ProductUpdate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

### Referencias no verificadas

Referencias no verificadas para: .py. El analisis estatico no cubre esos lenguajes: que no se haya listado nada NO garantiza que no haya referencias colgando.

## Como saber que terminaste

```bash
(cd api && pip install -r requirements.txt && python -m compileall -q app && python -c "import app") && (cd data && pip install -e . && python src/main.py)
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Tecnología Python, Advanced L2

### Brecha de conocimiento
Realiza por medio de un Framework sobre su lenguaje de programacion primario, enrutamiento de peticiones, consultas, creación de un API REST., Realiza por medio de un Framework sobre su lenguaje de programacion primario, enrutamiento de peticiones, consultas, creación de un API REST.

### Reto
- Tema: Representational State Transfer (REST)
- Seniority: advanced-l2
- Tipo: practical
- Título: Construcción de una API REST para gestión de productos
- Tiempo estimado: 10 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición del modelo de producto — objetivo: Definir el modelo de producto con sus atributos y restricciones. — entregable (NO resolver): Modelo de producto definido con sus atributos y restricciones.
- Fase 2: Implementación de endpoints CRUD — objetivo: Implementar los endpoints para crear, leer, actualizar y eliminar productos. — entregable (NO resolver): Endpoints REST implementados para las operaciones CRUD sobre productos.
- Fase 3: Manejo de casos límite y errores — objetivo: Manejar adecuadamente los casos límite y errores del dominio. — entregable (NO resolver): Lógica implementada para manejar casos límite y errores del dominio.
- Fase 4: Optimización y refactorización — objetivo: Optimizar y refactorizar la implementación de la API REST. — entregable (NO resolver): Implementación optimizada y refactorizada de la API REST.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (entrega de archivos).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Entrega de archivos
Entregá cada archivo con su ruta completa, respetando exactamente la estructura de rutas
indicada por los marcadores: un bloque por archivo, precedido por su ruta. No generes ZIPs
ni archivos adjuntos.
La entrega debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: Entregá los archivos completos al finalizar. No preguntes si el usuario
quiere recibirlos. Simplemente entregalos; No debes desplegar en el chat el resumen de lo que arreglaste, solo entregá los archivos.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del último archivo entregado
No preguntes si el usuario quiere los archivos: simplemente entregalos siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: api/main.py ===
from fastapi import FastAPI
from app.app import create_app
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

app: FastAPI = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        reload=os.getenv("ENVIRONMENT", "development") == "development"
    )

// === ARCHIVO: api/requirements.txt ===
fastapi==0.162.4
uvicorn==0.54.0
pydantic==2.14.3
pytest==9.2.0
httpx==0.28.1
asyncpg==0.32.0
psycopg2-binary==2.9.13
pytest-asyncio==1.5.0
python-dotenv==1.2.4
sqlalchemy==2.1.9

// === ARCHIVO: api/app/domain/models.py ===
from pydantic import BaseModel, Field, validator
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category: str = Field(..., min_length=1, max_length=50)

    @validator('name')
    def name_must_be_unique(cls, v):
        # Validación de unicidad se manejará en la capa de aplicación
        return v

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    category: Optional[str] = Field(None, min_length=1, max_length=50)

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class ProductInDB(Product):
    pass

// === ARCHIVO: api/app/domain/exceptions.py ===
class ProductNotFoundError(Exception):
    """Excepción lanzada cuando un producto no es encontrado."""
    def __init__(self, product_id: int):
        self.product_id = product_id
        super().__init__(f"Product with id {product_id} not found")

class ProductAlreadyExistsError(Exception):
    """Excepción lanzada cuando se intenta crear un producto con un nombre que ya existe."""
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Product with name {name} already exists")

class InvalidProductDataError(Exception):
    """Excepción lanzada cuando los datos del producto son inválidos."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class DatabaseError(Exception):
    """Excepción lanzada cuando ocurre un error en la base de datos."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

// === ARCHIVO: api/app/domain/repositories.py ===
from typing import Protocol, List, Optional
from .models import Product, ProductCreate, ProductUpdate

class ProductRepository(Protocol):
    async def create(self, product_create: ProductCreate) -> Product:
        """Crea un nuevo producto en la base de datos."""
        ...

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        """Obtiene un producto por su ID."""
        ...

    async def get_by_name(self, name: str) -> Optional[Product]:
        """Obtiene un producto por su nombre."""
        ...

    async def update(self, product_id: int, product_update: ProductUpdate) -> Optional[Product]:
        """Actualiza un producto existente."""
        ...

    async def delete(self, product_id: int) -> bool:
        """Elimina un producto por su ID."""
        ...

    async def list_all(self) -> List[Product]:
        """Lista todos los productos."""
        ...

// === ARCHIVO: api/app/application/services.py ===
# TODO(reto): archivo stubbeado; implementa los cuerpos.
from typing import List, Optional
from ..domain.models import Product, ProductCreate, ProductUpdate
from ..domain.repositories import ProductRepository
from ..domain.exceptions import ProductNotFoundError, ProductAlreadyExistsError, InvalidProductDataError

# TODO(reto): Implementar la lógica de negocio para gestionar productos
class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def create_product(self, product_create: ProductCreate) -> Product:
        raise NotImplementedError("TODO(reto): create_product")
    async def get_product(self, product_id: int) -> Product:
        raise NotImplementedError("TODO(reto): get_product")
    async def update_product(self, product_id: int, product_update: ProductUpdate) -> Product:
        raise NotImplementedError("TODO(reto): update_product")
    async def delete_product(self, product_id: int) -> None:
        raise NotImplementedError("TODO(reto): delete_product")
    async def list_products(self) -> List[Product]:
        raise NotImplementedError("TODO(reto): list_products")

// === ARCHIVO: api/app/infrastructure/repositories.py ===
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from ..domain.models import Product, ProductCreate, ProductUpdate, ProductInDB
from ..domain.repositories import ProductRepository
from ..domain.exceptions import ProductNotFoundError, ProductAlreadyExistsError, DatabaseError
from sqlalchemy import update as sql_update, delete as sql_delete

class SQLAlchemyProductRepository(ProductRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, product_create: ProductCreate) -> Product:
        try:
            existing_product = await self.get_by_name(product_create.name)
            if existing_product:
                raise ProductAlreadyExistsError(product_create.name)

            product_in_db = ProductInDB(**product_create.model_dump())
            self.session.add(product_in_db)
            await self.session.flush()
            await self.session.refresh(product_in_db)
            return Product.model_validate(product_in_db)
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise DatabaseError(f"Error creating product: {str(e)}")

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        try:
            result = await self.session.execute(
                select(ProductInDB).where(ProductInDB.id == product_id)
            )
            product_in_db = result.scalars().first()
            return Product.model_validate(product_in_db) if product_in_db else None
        except SQLAlchemyError as e:
            raise DatabaseError(f"Error getting product by id: {str(e)}")

    async def get_by_name(self, name: str) -> Optional[Product]:
        try:
            result = await self.session.execute(
                select(ProductInDB).where(ProductInDB.name == name)
            )
            product_in_db = result.scalars().first()
            return Product.model_validate(product_in_db) if product_in_db else None
        except SQLAlchemyError as e:
            raise DatabaseError(f"Error getting product by name: {str(e)}")

    async def update(self, product_id: int, product_update: ProductUpdate) -> Optional[Product]:
        try:
            product = await self.get_by_id(product_id)
            if not product:
                raise ProductNotFoundError(product_id)

            update_data = product_update.model_dump(exclude_unset=True)
            if not update_data:
                return product

            await self.session.execute(
                sql_update(ProductInDB)
                .where(ProductInDB.id == product_id)
                .values(**update_data)
            )
            await self.session.flush()

            updated_product = await self.get_by_id(product_id)
            return updated_product
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise DatabaseError(f"Error updating product: {str(e)}")

    async def delete(self, product_id: int) -> bool:
        try:
            product = await self.get_by_id(product_id)
            if not product:
                raise ProductNotFoundError(product_id)

            await self.session.execute(
                sql_delete(ProductInDB).where(ProductInDB.id == product_id)
            )
            await self.session.flush()
            return True
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise DatabaseError(f"Error deleting product: {str(e)}")

    async def list_all(self) -> List[Product]:
        try:
            result = await self.session.execute(select(ProductInDB))
            products_in_db = result.scalars().all()
            return [Product.model_validate(p) for p in products_in_db]
        except SQLAlchemyError as e:
            raise DatabaseError(f"Error listing products: {str(e)}")

// === ARCHIVO: api/app/infrastructure/database.py ===
# TODO(reto): archivo stubbeado; implementa los cuerpos.
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.asyncio import AsyncAttrs
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/products_db")

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

class ProductModel(Base, AsyncAttrs):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String, nullable=False)

async def init_db():
    raise NotImplementedError("TODO(reto): init_db")
async def get_db() -> AsyncSession:
    raise NotImplementedError("TODO(reto): get_db")

// === ARCHIVO: api/app/api/dependencies.py ===
"""Dependencias inyectables para FastAPI."""

from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_db
from app.infrastructure.repositories import SQLAlchemyProductRepository
from app.domain.repositories import ProductRepository
from app.application.services import ProductService


async def get_product_repository(
    db: AsyncSession = Depends(get_db)
) -> ProductRepository:
    """Inyecta una instancia del repositorio de productos."""
    return SQLAlchemyProductRepository(session=db)


async def get_product_service(
    repository: ProductRepository = Depends(get_product_repository)
) -> ProductService:
    """Inyecta una instancia del servicio de productos."""
    return ProductService(repository=repository)

// === ARCHIVO: api/app/api/routers.py ===
# TODO(reto): archivo stubbeado; implementa los cuerpos.
"""Routers de la API REST para gestión de productos.

Este módulo define los endpoints HTTP para las operaciones CRUD
sobre productos. La implementación de la lógica de negocio se
delega al servicio de productos inyectado como dependencia.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from app.domain.models import Product, ProductCreate, ProductUpdate
from app.domain.exceptions import ProductNotFoundError
from app.application.services import ProductService
from app.api.dependencies import get_product_service


router = APIRouter(prefix="/products", tags=["products"])


@router.post("", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_data: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    raise NotImplementedError("TODO(reto): create_product")
@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):
    raise NotImplementedError("TODO(reto): get_product")
@router.put("/{product_id}", response_model=Product)
async def update_product(
    product_id: int,
    product_data: ProductUpdate,
    service: ProductService = Depends(get_product_service)
):
    raise NotImplementedError("TODO(reto): update_product")
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):
    raise NotImplementedError("TODO(reto): delete_product")
@router.get("", response_model=List[Product])
async def list_products(
    service: ProductService = Depends(get_product_service)
):
    raise NotImplementedError("TODO(reto): list_products")

// === ARCHIVO: api/app/app.py ===
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

// === ARCHIVO: data/pyproject.toml ===
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "skeleton"
version = "0.0.0"
dependencies = ["sqlalchemy==2.1.9", "alembic==1.20.1", "psycopg2-binary==2.9.13", "pydantic==2.14.4", "python-dotenv==1.2.4"]

// === ARCHIVO: data/src/infrastructure/__init__.py ===
# Infrastructure root sample

// === ARCHIVO: data/src/infrastructure/database.py ===
# Database configuration sample
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

// === ARCHIVO: data/src/main.py ===
# Entry point
from sqlalchemy.orm import Session
from infrastructure.database import SessionLocal

def main():
    db: Session = SessionLocal()
    print("Skeleton compiles successfully")

if __name__ == "__main__":
    main()

// === ARCHIVO: data/src/contracts/__init__.py ===
# Contracts root sample

// === ARCHIVO: data/src/domain/models/product.py ===
from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, validator
from typing import Optional

Base = declarative_base()

class ProductModel(Base):
    __tablename__ = 'products'
    __table_args__ = (
        CheckConstraint('price >= 0', name='check_price_non_negative'),
        CheckConstraint('stock >= 0', name='check_stock_non_negative')
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String, nullable=False)

    def __init__(self, name: str, price: float, stock: int, category: str):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category: str

    @validator('price')
    def price_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Price must be non-negative')
        return v

    @validator('stock')
    def stock_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Stock must be non-negative')
        return v

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int
    category: str

    @validator('price')
    def price_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Price must be non-negative')
        return v

    @validator('stock')
    def stock_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('Stock must be non-negative')
        return v

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[str] = None

    @validator('price')
    def price_must_be_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError('Price must be non-negative')
        return v

    @validator('stock')
    def stock_must_be_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError('Stock must be non-negative')
        return v

// === ARCHIVO: data/src/domain/repositories/product_repository.py ===
from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.product import ProductModel, Product, ProductCreate, ProductUpdate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product_create: ProductCreate) -> Product:
        db_product = ProductModel(
            name=product_create.name,
            price=product_create.price,
            stock=product_create.stock,
            category=product_create.category
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return Product(
            id=db_product.id,
            name=db_product.name,
            price=db_product.price,
            stock=db_product.stock,
            category=db_product.category
        )

    def get_product(self, product_id: int) -> Optional[Product]:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if db_product:
            return Product(
                id=db_product.id,
                name=db_product.name,
                price=db_product.price,
                stock=db_product.stock,
                category=db_product.category
            )
        return None

    def update_product(self, product_id: int, product_update: ProductUpdate) -> Optional[Product]:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not db_product:
            return None

        if product_update.name is not None:
            db_product.name = product_update.name
        if product_update.price is not None:
            db_product.price = product_update.price
        if product_update.stock is not None:
            db_product.stock = product_update.stock
        if product_update.category is not None:
            db_product.category = product_update.category

        self.db.commit()
        self.db.refresh(db_product)
        return Product(
            id=db_product.id,
            name=db_product.name,
            price=db_product.price,
            stock=db_product.stock,
            category=db_product.category
        )

    def delete_product(self, product_id: int) -> bool:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not db_product:
            return False

        self.db.delete(db_product)
        self.db.commit()
        return True

    def list_products(self) -> List[Product]:
        db_products = self.db.query(ProductModel).all()
        return [
            Product(
                id=product.id,
                name=product.name,
                price=product.price,
                stock=product.stock,
                category=product.category
            )
            for product in db_products
        ]

// === ARCHIVO: data/src/domain/migrations/env.py ===
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from ...infrastructure.database import Base
import os
from dotenv import load_dotenv

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

load_dotenv()
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

// === ARCHIVO: data/src/domain/migrations/versions/initial_migration.py ===
"""Initial migration

Revision ID: 123456789abc
Revises:
Create Date: 2023-01-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '123456789abc'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('stock', sa.Integer(), nullable=False),
        sa.Column('category', sa.String(), nullable=False),
        sa.CheckConstraint('price >= 0', name='check_price_non_negative'),
        sa.CheckConstraint('stock >= 0', name='check_stock_non_negative')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=True)

def downgrade() -> None:
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
```
