from app.repositories.customer_repository import CustomerRepository
from app.domain.exceptions import UserIdAlreadyExists
from app.models import Customer

class CustomerService:
    
    @classmethod
    def _ensure_user_id_available(cls, user_id):
        if CustomerRepository.user_exists(user_id):
            raise UserIdAlreadyExists()
        
    @classmethod
    def register_customer(cls, user_id: int, name: str, phone: str, address: str) -> Customer:
        cls._ensure_user_id_available(user_id)
        return CustomerRepository.register(user_id, name, phone, address)