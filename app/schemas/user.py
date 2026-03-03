from enum import Enum
from pydantic import BaseModel, EmailStr

from app.schemas import ResponseModel

class UserRole(str, Enum):
    admin = 'admin'
    customer = 'customer'

class UserActivity(str, Enum):
    active = "active"
    inactive = "inactive"

class CreateUserCustomer(BaseModel):
    email: EmailStr
    password: str
    name: str
    phone: str
    address: str

class CreateUserAdmin(BaseModel):
    email: EmailStr
    password: str

class UserChangePassword(BaseModel):
    password: str

class UserChangeIsActive(BaseModel):
    is_active: UserActivity

class UserResponseModel(ResponseModel):
    id: int
    email: EmailStr
    role: str
    is_active: bool

class UserCustomerResponseModel(ResponseModel):
    user_id: UserResponseModel
    name: str
    phone: str
    address: str
