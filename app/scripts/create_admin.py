import os

from app.database import database as connection
from app.models import User
from app.security.hashing import hash_password

from dotenv import load_dotenv

load_dotenv()

def create_admin():
    if connection.is_closed():
        connection.connect()

    admin_exists = User.select().where(User.role == "admin").exists()

    if admin_exists:
        print("Ya existe un administrador.")
        return

    User.create(
        email=os.getenv('ADMIN_USER_EMAIL'),
        password=hash_password(os.getenv('ADMIN_USER_PASSWORD')),
        role="admin"
    )

    print("Administrador creado correctamente.")

    connection.close()

if __name__ == "__main__":
    create_admin()