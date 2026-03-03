from peewee import *
from app.database import database
from datetime import datetime

class Product(Model):
    name = CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = IntegerField(constraints=[Check('stock >= 0')])
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = database
        table_name = 'products'
