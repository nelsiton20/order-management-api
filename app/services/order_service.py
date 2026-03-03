from app.repositories.order_repository import OrderRepository
from app.repositories.order_item_repository import OrderItemRepository
from app.services.product_service import ProductService
from app.services.order_item_service import OrderItemService
from app.domain.exceptions import OrderNotFound
from app.models import Order, User
from app.database import database
from app.domain.rules.order_rules import OrderRules

class OrderService:

    @classmethod
    def _get_order_or_fail(cls, order_id: int) -> Order:
        order = OrderRepository.get_by_id(order_id)
        if order is None:
            raise OrderNotFound()
        return order

    @classmethod
    def create_order(cls, customer_id: int, order_items: list, user: User):
        with database.atomic():
            OrderRules.validate_user_availability(user)
            order = OrderRepository.create(customer_id)

            total = 0
            for item in order_items:
                product = ProductService.get_product(item.product_id)

                OrderRules.validate_product_availability(product)
                OrderRules.stock_available(product, item.quantity)

                subtotal = product.price * item.quantity
                OrderItemService.create_order_item(order.id, product.id, item.quantity, product.price, subtotal)
                total += subtotal
            
            return OrderRepository.update_total(order, total)

    @classmethod
    def get_order(cls, order_id: int):
        return cls._get_order_or_fail(order_id)
    
    @classmethod
    def update_status(cls, order_id: int, status: str):
        with database.atomic():
            order = cls._get_order_or_fail(order_id)
            return OrderRepository.update_status(order, status)
        
    @classmethod
    def cancel_order(cls, order_id: int):
        with database.atomic():
            order = cls._get_order_or_fail(order_id)
            OrderRules.validate_order_cancellation(order)
            OrderRepository.update_status(order, 'cancelled')
            
            for item in order.order_items:
                ProductService.product_restore_stock(item.product_id, item.quantity)

    @classmethod
    def get_order_by_customer_id(cls, customer_id: int, page: int = 1, limit: int = 10):
        return OrderRepository.get_by_customer_id(customer_id, page, limit)
