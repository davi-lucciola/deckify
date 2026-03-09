from fastapi import Request
from fastapi.responses import JSONResponse

from app.domain.exceptions.deck_exceptions import DeckValidationError


async def deck_validation_handler(request: Request, exc: Exception) -> JSONResponse:
    assert isinstance(exc, DeckValidationError)
    return JSONResponse(status_code=422, content={'detail': str(exc)})
