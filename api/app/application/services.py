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