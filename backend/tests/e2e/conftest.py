from collections.abc import AsyncGenerator, Generator

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from testcontainers.postgres import PostgresContainer  # type: ignore

from app.infra.database.session import Base, get_db
from app.main import app


@pytest.fixture(scope='session')
def postgres_container() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer('postgres:16-alpine') as container:
        yield container


@pytest.fixture(scope='session')
async def test_engine(
    postgres_container: PostgresContainer,
) -> AsyncGenerator[AsyncEngine, None]:
    sync_url: str = postgres_container.get_connection_url()
    async_url: str = sync_url.replace(
        'postgresql+psycopg2://', 'postgresql+asyncpg://', 1
    )
    async_url = async_url.replace('postgresql://', 'postgresql+asyncpg://', 1)

    engine = create_async_engine(async_url, echo=False, pool_pre_ping=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest.fixture(scope='session', autouse=True)
def override_get_db(test_engine: AsyncEngine) -> Generator[None, None, None]:
    async def _get_db() -> AsyncGenerator[AsyncSession, None]:
        async with AsyncSession(test_engine, expire_on_commit=False) as db:
            try:
                yield db
            except Exception as err:
                await db.rollback()
                raise err
            finally:
                await db.close()

    app.dependency_overrides[get_db] = _get_db
    yield
    app.dependency_overrides.clear()


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url='http://test', follow_redirects=True
    ) as async_client:
        yield async_client
