# Python Backend Rules

## Code Style

- Line length: 88, indent width: 4
- String quotes: single quotes (enforced by ruff format)
- Ruff lint rules enabled: `I` (isort), `F` (pyflakes), `E`/`W` (pycodestyle), `PL` (pylint), `PT` (pytest)
- Ignored rules: `PLR0913`, `PLR0917` (too-many-arguments — intentionally allowed)
- Run `task format` (ruff check --fix + ruff format) before committing

## Type Annotations

- All functions must have full type annotations (mypy strict mode is enforced)
- Use Python 3.12+ `type X = ...` syntax for type aliases
- Example: `type SQLAlchemy = Annotated[AsyncSession, Depends(get_db)]`

## Async-First

- All route handlers, services, and repository methods must be `async def`
- Never use sync wrappers around async functions

## FastAPI / Dependency Injection

- Declare dependencies as `Annotated` type aliases in `app/dependencies.py`
- Never inline `Depends(...)` directly in route function signatures

## Module Conventions

- `app/routers/` — HTTP layer only; no business logic
- `app/services/` — Business logic; raise domain exceptions (not HTTP-aware)
- `app/repositories/` — DB queries; accept `AsyncSession`, return domain objects
- `app/models/` — SQLAlchemy models extending `Base` from `app/database.py`
- `app/schemas/` — Pydantic models for request/response serialization

## Error Handling

- Routers catch exceptions and raise `HTTPException`
- Services raise domain-level exceptions (not HTTP-aware)

## Testing

- Use `TestClient` fixture from `tests/conftest.py`
- Async fixtures use `pytest-asyncio`
- Coverage must stay >= 90% (omitting `config.py`, `database.py`, `dependencies.py`)
- Run with `task test`
