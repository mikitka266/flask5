from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name_product: str = Field(max_length=128)
    properties: str = Field(max_length=128)
    price: float


class ProductIn(BaseModel):
    id: int
    name_product: str = Field(max_length=128)
    properties: str = Field(max_length=128)
    price: float