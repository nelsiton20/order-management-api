from app.models import Customer

class CustomerRepository:
    @staticmethod
    def user_exists(user_id: int) -> bool:
        return Customer.select().where(Customer.user_id == user_id).exists()

    @staticmethod
    def register(user_id: int, name: str, phone: str, address: str) -> Customer:
        return Customer.create(
            user_id=user_id,
            name=name,
            phone=phone,
            address=address
        )

