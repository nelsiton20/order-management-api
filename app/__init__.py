from fastapi import FastAPI

from app.database import database as connection
from app.core.exception_handlers import domain_exception_handler, generic_exception_handler
from app.domain.exceptions import DomainError
from app.routers import api_v1
from app.models import User, Customer, Product, Order, OrderItem

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    if connection.is_closed():
        connection.connect()
        print('CONEXIÓN EXITOSA')
    
    connection.create_tables([User, Customer, Product, Order, OrderItem])
    yield
    if not connection.is_closed():
        connection.close()
        print('CONEXIÓN CERRADA')

app = FastAPI(lifespan=lifespan)

app.add_exception_handler(DomainError, domain_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(api_v1)