from peewee import *

from app.database import database
from app.models import Customer

from datetime import datetime

class Order(Model):
    customer_id = ForeignKeyField(Customer, backref='orders')
    status = CharField(
        max_length=20,
        constraints=[
            Check("status IN ('pending', 'confirmed', 'shipped', 'delivered', 'cancelled')")
        ],
        default='pending'
    )
    total = DecimalField(max_digits=10, decimal_places=2, constraints=[Check('total >= 0')])
    created_at = DateTimeField(default=datetime.now)
    
    class Meta:
        database = database
        table_name = 'orders'
