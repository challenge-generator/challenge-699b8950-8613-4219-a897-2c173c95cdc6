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