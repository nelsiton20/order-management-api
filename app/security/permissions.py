from app.models import User
from app.security.auth import get_current_user

from fastapi import Depends, status, HTTPException

def require_role(required_role: str):
    def checker(user: User = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='No tienes permisos para realizar esta acción'
            )
        return user
    
    return checker