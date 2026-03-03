from app.models import Order

class OrderRepository:
    
    @staticmethod
    def create(customer_id: int) -> Order:
        return Order.create(
            customer_id=customer_id,
            total=0
        )
    
    @staticmethod
    def get_by_id(order_id: int):
        return Order.select().where(Order.id == order_id).first()
    
    @staticmethod
    def update_status(order: Order, status: str) -> Order:
        order.status = status
        order.save()
        return order
    
    @staticmethod
    def update_total(order: Order, total: float) -> Order:
        order.total = total
        order.save()
        return order
    
    @staticmethod
    def get_by_customer_id(customer_id: int, page: int = 1, limit: int = 10) -> list[Order]:
        return Order.select().where(Order.customer_id == customer_id).paginate(page, limit)
