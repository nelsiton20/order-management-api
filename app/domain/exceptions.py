class DomainError(Exception):
    status_code = 400
    default_message = 'Error de dominio'

class EmailAlreadyExists(DomainError):
    status_code = 409
    default_message = 'El email ya está en uso'

class UserNotFound(DomainError):
    status_code = 404
    default_message = 'Usuario no encontrado'

class InvalidCredentials(DomainError):
    status_code = 401
    default_message = 'Credenciales inválidas'

class UserIdAlreadyExists(DomainError):
    status_code = 409
    default_message = 'Un customer ya está registrado con el user_id enviado'


# PRODUCT EXCEPTIONS
class ProductNotFound(DomainError):
    status_code = 404
    default_message = 'Producto no encontrado'

# ORDER EXCEPTIONS
class OrderNotFound(DomainError):
    status_code = 404
    default_message = 'Orden no encontrada'

# REGLAS DE NEGOCIO
class ProductOfOutStock(DomainError):
    status_code = 409 
    default_message = "El producto no cuenta con stock"

class ProductWithoutStockNecessary(DomainError):
    status_code = 409
    default_message = "Producto sin stock necesario"

class InvalidOrderStateError(DomainError):
    status_code = 409
    default_message = "El pedido no se puede cancelar debido a su estado actual"

class InactiveProductError(DomainError):
    status_code = 409
    default_message = 'El producto no está activo'

class InactiveUserError(DomainError):
    status_code = 409
    default_message = 'El usuario no está activo'
