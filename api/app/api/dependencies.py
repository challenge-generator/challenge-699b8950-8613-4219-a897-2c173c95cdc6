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