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