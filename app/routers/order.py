from fastapi import APIRouter, Depends, status

from app.models import User
from app.security.auth import get_current_user
from app.services.order_service import OrderService
from app.schemas.order import OrderResponseModel, CreateOrder, UpdateStatusOder
from app.security.permissions import require_role
from app.security.ownership import require_order_owner_or_admin

router = APIRouter(prefix='/orders')

@router.post('/', response_model=OrderResponseModel, summary='Crear una nueva orden')
async def create_order(order_request: CreateOrder, user: User = Depends(get_current_user)):
    return OrderService.create_order(user.customer.first().id, order_request.order_items, user)

@router.get('/my-orders', response_model=list[OrderResponseModel], summary='Obtener mis ordenes')
async def get_my_orders(page: int = 1, limit: int = 10, user: User = Depends(get_current_user)):
    return OrderService.get_order_by_customer_id(user.customer.first().id, page, limit)

@router.get('/{order_id}',
            response_model=OrderResponseModel,
            dependencies=[Depends(require_order_owner_or_admin)],
            summary='Obtener una orden por su ID')
async def get_order(order_id: int):
    return OrderService.get_order(order_id)

@router.patch('/{order_id}/status',
              response_model=OrderResponseModel,
              dependencies=[Depends(require_role('admin'))],
              summary='Actualizar el estado de una orden')
async def update_status_order(order_id: int, order_request: UpdateStatusOder):
    return OrderService.update_status(order_id, order_request.status)

@router.patch('/{order_id}/cancel',
              dependencies=[Depends(require_order_owner_or_admin)],
              status_code=status.HTTP_204_NO_CONTENT,
              summary='Cancelar una orden')
async def cancel_order(order_id: int):
    OrderService.cancel_order(order_id)
