from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.models import User
from app.security.jwt_handler import decode_access_token

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth')

def get_current_user(token: str = Depends(oauth2_schema)) -> User:
    payload = decode_access_token(token)

    if payload:
        user = User.select().where(User.id == payload['sub']).first()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Usuario no encontrado'
            )
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Access token no válido',
            headers={'WWW-Authenticate': 'Bearer'}
        )