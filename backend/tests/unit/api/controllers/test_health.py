from app.api.controllers.health_controller import health_check
from app.api.schemas.health_schema import HealthOut


def test_health_check_returns_ok() -> None:
    result = health_check()
    assert result == HealthOut(status='ok')
