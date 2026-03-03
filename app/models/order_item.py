from datetime import datetime
from peewee import *

from app.database import database
from app.models import Order, Product

class OrderItem(Model):
    order_id = ForeignKeyField(Order, backref='order_items')
    product_id = ForeignKeyField(Product, backref='order_items')
    quantity = IntegerField(constraints=[Check('quantity >= 1')])
    unit_price = DecimalField(max_digits=10, decimal_places=2)
    subtotal = DecimalField(max_digits=10, decimal_places=2)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = database
        table_name = 'order_items'
