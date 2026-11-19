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