from peewee import *

from app.database import database
from app.models import User

from datetime import datetime

class Customer(Model):
    user_id = ForeignKeyField(User, backref='customer', unique=True, on_delete='CASCADE')
    name = CharField(max_length=100)
    phone = CharField(max_length=9)
    address = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = database
        table_name = 'customers'
