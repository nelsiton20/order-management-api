from app.models import Product
from app.repositories.product_repository import ProductRepository
from app.database import database
from app.domain.exceptions import ProductNotFound

class ProductService:
    @classmethod
    def _get_product_or_fail(cls, product_id: int) -> Product:
        product = ProductRepository.get_by_id(product_id)
        if product is None:
            raise ProductNotFound()
        return product

    @classmethod
    def register_product(cls, name: str, price: float, stock: int):
        with database.atomic():
            return ProductRepository.create(name, price, stock)
        
    @classmethod
    def get_product(cls, product_id: int):
        return cls._get_product_or_fail(product_id)
    
    @classmethod
    def get_all_products(cls, page: int = 1, limit: int = 10):
        return ProductRepository.get_all(page, limit)
    
    @classmethod
    def delete_product(cls, product_id: int):
        with database.atomic():
            product = cls._get_product_or_fail(product_id)
            ProductRepository.delete(product)
            return product  
        
    @classmethod
    def product_reduce_stock(cls, product_id: int, quantity):
        with database.atomic():
            product = cls._get_product_or_fail(product_id)
            ProductRepository.reduce_stock(product, quantity)

    @classmethod
    def product_restore_stock(cls, product_id: int, quantity: int):
        product = cls._get_product_or_fail(product_id)
        ProductRepository.restore_stock(product, quantity)
