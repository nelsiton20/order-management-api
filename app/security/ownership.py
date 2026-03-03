from fastapi import Depends, HTTPException, status

from app.models import User, Order
from app.security.auth import get_current_user

def require_owner_or_admin(user_id: int, user: User = Depends(get_current_user)):
    if user.role == "admin":
        return user
    
    if user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='No tienes permisos para modificar este recurso'
        )
    
    return user

def require_order_owner_or_admin(order_id: int, user: User = Depends(get_current_user)):
    if user.role == "admin":
        return user

    try:
        order = Order.get_by_id(order_id)
    except Order.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Orden no encontrada"
        )

    customer = order.customer_id 
    
    if customer.user_id.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para cancelar esta orden"
        )

    return user