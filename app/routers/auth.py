from fastapi import APIRouter, Depends

from app.schemas.auth import LoginUser
from app.schemas.user import UserResponseModel
from app.models import User
from app.services.auth_service import AuthService
from app.security import get_current_user, create_access_token

router = APIRouter(prefix='/auth')

@router.post('/login')
async def login(data: LoginUser):
    user = AuthService.authenticate(data.email, data.password)
    access_token = create_access_token(user.id, user.role)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get('/me', response_model=UserResponseModel)
async def get_me(user: User = Depends(get_current_user)):
    return user
