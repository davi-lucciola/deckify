from fastapi import APIRouter

from app.api.schemas.health_schema import HealthOut

health_router = APIRouter(tags=['Infra'])


@health_router.get('/health', summary='Health Check')
def health_check() -> HealthOut:
    """Returns the health status of the API."""
    return HealthOut(status='ok')
