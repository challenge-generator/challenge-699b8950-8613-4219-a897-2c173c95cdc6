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