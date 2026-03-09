import pytest
from pydantic import ValidationError

from app.api.schemas.health import HealthOut


def test_health_out_valid() -> None:
    schema = HealthOut(status='ok')
    assert schema.status == 'ok'


def test_health_out_serialization() -> None:
    schema = HealthOut(status='ok')
    assert schema.model_dump() == {'status': 'ok'}


def test_health_out_missing_status_raises() -> None:
    with pytest.raises(ValidationError):
        HealthOut()  # type: ignore[call-arg]
