import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.anyio
async def test_health_check(client: AsyncClient) -> None:
    response = await client.get('/health')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'ok'}
