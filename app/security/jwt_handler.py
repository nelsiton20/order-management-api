import os
import jwt

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

def create_access_token(user_id: int, user_role: str):
    expire = datetime.now(timezone.utc) + timedelta(days=int(os.getenv('ACCESS_TOKEN_EXPIRE_DAYS')))

    payload = {
        "sub": str(user_id),
        "role": user_role,
        "exp": expire
    }

    return jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))

def decode_access_token(token: str):
    try:
        return jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
