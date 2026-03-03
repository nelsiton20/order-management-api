from pydantic import BaseModel
from app.schemas import ResponseModel
from app.schemas.product import ProductResponseModel

class CreateOrderItem(BaseModel):
    product_id: int
    quantity: int

class OrderItemResponseModel(ResponseModel):
    id: int
    product_id: ProductResponseModel
    quantity: int
    unit_price: float
    subtotal: float
    