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