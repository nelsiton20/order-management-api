from app.models import User, Customer
from app.repositories.user_repository import UserRepository
from app.repositories.customer_repository import CustomerRepository
from app.domain.exceptions import EmailAlreadyExists, UserNotFound
from app.database import database
from app.security.hashing import hash_password
from app.services.customer_service import CustomerService

class UserService:

    @classmethod
    def _get_user_or_fail(cls, user_id: int) -> User:
        user = UserRepository.get_by_id(user_id)
        if user is None:
            raise UserNotFound()
        return user

    @classmethod
    def _ensure_email_available(cls, email: str, exclude_id: int = None):
        if UserRepository.email_exists(email, exclude_id):
            raise EmailAlreadyExists()

    @classmethod
    def _create_hashed_password(cls, password: str) -> str:
        return hash_password(password)

    @classmethod
    def register_admin(cls, email: str, password: str) -> User:
        with database.atomic():
            cls._ensure_email_available(email)
            return UserRepository.create_user(email, cls._create_hashed_password(password), 'admin')
        
    @classmethod
    def register_customer(cls, email: str, password: str, name: str, phone: str, address: str):
        with database.atomic():
            cls._ensure_email_available(email)
            user = UserRepository.create_user(email, cls._create_hashed_password(password), 'customer')
            return CustomerService.register_customer(user.id, name, phone, address)
        
    @classmethod
    def change_password(cls, user_id: int, password: str) -> User:
        with database.atomic():
            user = cls._get_user_or_fail(user_id)
            user.password = cls._create_hashed_password(password)
            user.save()
            return user
        
    @classmethod
    def update_user_activity_status(cls, user_id: int, active: bool):
        with database.atomic():
            user = cls._get_user_or_fail(user_id)
            return UserRepository.update_active_state(user, active)
    
    @classmethod
    def delete_user(cls, user_id: int):
        with database.atomic():
            user = cls._get_user_or_fail(user_id)
            UserRepository.delete(user)
            return user