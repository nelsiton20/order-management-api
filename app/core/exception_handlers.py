import traceback
from fastapi import Request
from fastapi.responses import JSONResponse

from app.domain.exceptions import DomainError
from app.core.logger import logger

async def domain_exception_handler(request: Request, exc: DomainError):
    logger.warning(
        f"{exc.__class__.__name__} | "
        f"path={request.url.path} | "
        f"method={request.method}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.default_message
        }
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(
        f"UNHANDLED_EXCEPTION | "
        f"path={request.url.path} | "
        f"method={request.method}"
    )

    logger.error(traceback.format_exc())

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Error interno del servidor"
        }
    )