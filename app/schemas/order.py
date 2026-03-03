from enum import Enum
from pydantic import BaseModel
from app.schemas import ResponseModel
from app.schemas.order_item import CreateOrderItem, OrderItemResponseModel

class OrderStatus(str, Enum):
    pending = 'pending'
    confirmed = 'confirmed'
    shipped = 'shipped'
    delivered = 'delivered'

class CreateOrder(BaseModel):
    order_items: list[CreateOrderItem]

class OrderResponseModel(ResponseModel):
    id: int
    status: str
    total: float
    order_items: list[OrderItemResponseModel]

class UpdateStatusOder(BaseModel):
    status: OrderStatus
