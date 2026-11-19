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