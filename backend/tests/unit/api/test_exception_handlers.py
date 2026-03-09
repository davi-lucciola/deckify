import json
from unittest.mock import MagicMock

from fastapi import status

from app.api.exception_handlers import deck_validation_handler
from app.domain.exceptions.deck_exceptions import DeckValidationError


async def test_deck_validation_handler_returns_422() -> None:
    request = MagicMock()
    exc = DeckValidationError('Deck title cannot be empty')

    response = await deck_validation_handler(request, exc)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


async def test_deck_validation_handler_returns_exception_message() -> None:
    request = MagicMock()
    exc = DeckValidationError('Deck title cannot be empty')

    response = await deck_validation_handler(request, exc)

    body = json.loads(response.body)
    assert body['detail'] == 'Deck title cannot be empty'
