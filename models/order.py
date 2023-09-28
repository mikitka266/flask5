from pydantic import BaseModel, Field
import date


class Order(BaseModel):
    id: int
    id_user: int
    id_product: int
    date_order: date
    status: str = Field(max_length=128)


class OrderIn(BaseModel):
    id_product: int
    date_order: date
    status: str = Field(max_length=128)