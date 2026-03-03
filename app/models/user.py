from peewee import *
from app.database import database
from datetime import datetime

class User(Model):
    email = CharField(max_length=50, unique=True)
    password = TextField()
    role = CharField(
        max_length=20,
        constraints=[
            Check("role IN ('admin', 'customer')")
        ])
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = database
        table_name = 'users'
