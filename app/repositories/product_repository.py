from app.models import Product

class ProductRepository:

    @staticmethod
    def create(name: str, price: float, stock: int) -> Product:
        return Product.create(
            name=name,
            price=price,
            stock=stock
        )
    
    @staticmethod
    def get_by_id(product_id: int):
        return Product.select().where(Product.id == product_id).first()
    
    @staticmethod
    def get_all(page: int = 1, limit: int = 10):
        return Product.select().paginate(page, limit)
    
    @staticmethod
    def delete(product: Product):
        product.delete_instance()

    @staticmethod
    def reduce_stock(product: Product, quantity: int):
        product.stock = product.stock - quantity
        product.save()

    @staticmethod
    def restore_stock(product: Product, quantity: int):
        product.stock = product.stock + quantity
        product.save()
