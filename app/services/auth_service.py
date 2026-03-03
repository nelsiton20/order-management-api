from app.repositories.user_repository import UserRepository
from app.models import User
from app.security.hashing import verify_password
from app.domain.exceptions import InvalidCredentials

class AuthService:
    @classmethod
    def authenticate(cls, email: str, password: str) -> User:
        user = UserRepository.get_by_email(email)

        if not user or not verify_password(password, user.password):
            raise InvalidCredentials()
        
        return user