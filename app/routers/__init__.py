from fastapi import APIRouter

from app.routers.auth import router as auth_router
from app.routers.user import router as user_router
from app.routers.order import router as order_router
from app.routers.product import router as product_router

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(auth_router)
api_v1.include_router(user_router)
api_v1.include_router(product_router)
api_v1.include_router(order_router)
