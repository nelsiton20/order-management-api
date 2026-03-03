from fastapi import APIRouter, status, Depends

from app.schemas.user import CreateUserCustomer, UserCustomerResponseModel, UserChangePassword, CreateUserAdmin, UserResponseModel, UserChangeIsActive
from app.services.user_service import UserService
from app.security.ownership import require_owner_or_admin
from app.security.permissions import require_role

router = APIRouter(prefix='/users')

@router.post('/', 
             response_model=UserCustomerResponseModel,
             status_code=status.HTTP_201_CREATED,
             summary='Crear un nuevo usuario con rol customer')
async def create_user_customer(user_request: CreateUserCustomer):
    return UserService.register_customer(user_request.email, user_request.password, user_request.name, user_request.phone, user_request.address)

@router.post('/admin',
             response_model=UserResponseModel,
             dependencies=[Depends(require_role('admin'))],
             status_code=status.HTTP_201_CREATED,
             summary='Crear un usuario administrador')
async def create_user_admin(user_request: CreateUserAdmin):
    return UserService.register_admin(user_request.email, user_request.password)

@router.patch('/{user_id}/password',
              response_model=UserResponseModel,
              dependencies=[Depends(require_owner_or_admin)],
              summary="Cambiar contraseña")
async def change_password(user_id: int, user_request: UserChangePassword):
    return UserService.change_password(user_id, user_request.password)

@router.patch('/{user_id}/activity-status',
              response_model=UserResponseModel,
              dependencies=[Depends(require_owner_or_admin)],
              summary='Actualizar el estado de actividad del usuario')
async def active_user(user_id: int, user_request: UserChangeIsActive):
    return UserService.update_user_activity_status(user_id, True if user_request.is_active == "active" else False)

@router.delete('/{user_id}',
                dependencies=[Depends(require_role('admin'))],
                status_code=status.HTTP_204_NO_CONTENT,
                summary='Eliminar un usuario')
async def delete_user(user_id: int):
    UserService.delete_user(user_id)