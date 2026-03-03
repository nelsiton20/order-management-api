from fastapi import APIRouter, status, Depends

from app.schemas.product import CreateProduct, ProductResponseModel
from app.security.auth import get_current_user
from app.security.permissions import require_role
from app.models import User
from app.services.product_service import ProductService

router = APIRouter(prefix='/products')

@router.post('/',
             response_model=ProductResponseModel,
             status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(require_role('admin'))],
             summary='Crear un nuevo producto')
async def create_product(product_request: CreateProduct):
    return ProductService.register_product(product_request.name, product_request.price, product_request.stock)

@router.get('/', response_model=list[ProductResponseModel], summary='Obtener todos los productos')
async def get_products(page: int = 1, limit: int = 10, user: User = Depends(get_current_user)):
    return ProductService.get_all_products(page, limit)

@router.get('/{product_id}', response_model=ProductResponseModel, summary='Obtener un producto por su ID')
async def get_product(product_id: int, user: User = Depends(get_current_user)):
    return ProductService.get_product(product_id)

@router.delete('/{product_id}',
               status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(require_role('admin'))],
               summary='Eliminar un producto')
async def delete_product(product_id: int):
    ProductService.delete_product(product_id)
