from decimal import Decimal
from pydantic import BaseModel, Field
from app.schemas import ResponseModel

class CreateProduct(BaseModel):
    name: str = Field(max_length=100)
    price: Decimal = Field(max_digits=10, decimal_places=2)
    stock: int = Field(ge=0)

class ProductResponseModel(ResponseModel):
    id: int
    name: str
    price: Decimal
    stock: int
