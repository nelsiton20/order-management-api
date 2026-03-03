from app.repositories.order_item_repository import OrderItemRepository
from app.models.order_item import OrderItem
from app.database import database
from app.services.product_service import ProductService

class OrderItemService:
    @classmethod
    def create_order_item(cls, order_id: int, product_id: int, quantity: int, unit_price: float, subtotal: float):
        with database.atomic():
            ProductService.product_reduce_stock(product_id, quantity)
            return OrderItemRepository.create(order_id, product_id, quantity, unit_price, subtotal)