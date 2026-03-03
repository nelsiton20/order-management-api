from app.models.order_item import OrderItem

class OrderItemRepository:

    @staticmethod
    def create(order_id: int, product_id: int, quantity: int, unit_price: float, subtotal: float) -> OrderItem:
        return OrderItem.create(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal
        )
