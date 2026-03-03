from app.models import Product, Order, User
from app.domain.exceptions import ProductOfOutStock, ProductWithoutStockNecessary, InvalidOrderStateError, InactiveProductError, InactiveUserError

class OrderRules:
    
    @staticmethod
    def stock_available(product: Product, order_quantity: int):
        if product.stock == 0:
            raise ProductOfOutStock()
        if order_quantity > product.stock:
            raise ProductWithoutStockNecessary()

    @staticmethod
    def validate_order_cancellation(order: Order):
        non_cancellable_states = ['cancelled', 'shipped', 'delivered']
        if order.status in non_cancellable_states:
            raise InvalidOrderStateError()
        
    @staticmethod
    def validate_product_availability(product: Product):
        if not product.is_active:
            raise InactiveProductError()
        
    @staticmethod
    def validate_user_availability(user: User):
        if not user.is_active:
            raise InactiveUserError()
