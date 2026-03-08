from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from loguru import logger


async def validation_exception_handler(request: Request, exc: RequestValidationError):

    for erro in exc.errors():
        campo = erro["loc"][-1]
        mensagem = erro["msg"]

        logger.error(
            f"{request.url.path} | campo={campo} | erro={mensagem}"
        )

    return await request_validation_exception_handler(request, exc)