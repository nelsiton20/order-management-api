from app.models import User

class UserRepository:
    @staticmethod
    def get_by_id(user_id: int):
        return User.select().where(User.id == user_id).first()
    
    @staticmethod
    def get_by_email(user_email: str):
        return User.select().where(User.email == user_email).first()
    
    @staticmethod
    def email_exists(email: str, exclude_id: int = None) -> bool:
        query = User.select().where(User.email == email)
        if exclude_id:
            query = query.where(User.id != exclude_id)
        return query.exists()
    
    @staticmethod
    def create_user(email: str, password: str, role: str) -> User:
        return User.create(
            email=email,
            password=password,
            role=role
        )
    
    @staticmethod
    def update_active_state(user: User, active: bool) -> User:
        user.is_active = active
        user.save()
        return user

    @staticmethod
    def delete(user: User) -> None:
        user.delete_instance()
