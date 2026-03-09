---
paths:
  - "backend/**/*.py"
---

# Python Backend Rules

## Code Style

- Line length: 88, indent width: 4
- String quotes: single quotes (enforced by ruff format)
- Ruff lint rules enabled: `I` (isort), `F` (pyflakes), `E`/`W` (pycodestyle), `PL` (pylint), `PT` (pytest)
- Run `task format` (ruff check --fix + ruff format) before committing

## Type Annotations

- All functions must have full type annotations (mypy strict mode is enforced)
- Use regular assignment `X = Annotated[...]` for FastAPI dependency type aliases — the `type X = ...` (PEP 695) syntax breaks FastAPI's `get_type_hints()` resolution
- Never use `Any` unless absolutely necessary; prefer narrowing with `isinstance` or `TypeGuard`
- Prefer `Optional[X]` over `X | None`

## Naming Conventions

- Variables, functions, and modules: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: prefix with `_`

## General Best Practices

- Prefer early returns to reduce nesting
- Use list/dict/set comprehensions over `map`/`filter` when readable
- Prefer `pathlib.Path` over `os.path` for filesystem operations
- Use `dataclasses` or Pydantic models instead of raw dicts for structured data
- Prefer `@dataclass` over manual `__init__` to avoid boilerplate; use `field(default_factory=lambda: [])` for mutable defaults
- Avoid mutable default arguments; use `None` and initialize inside the function

## Async-First

- All I/O-bound operations must be `async def`
- Never use sync wrappers around async functions (e.g., `asyncio.run` inside a coroutine)
- Prefer `asyncio.gather` for concurrent independent async calls

## FastAPI

- Use `Annotated` for dependency injection — never inline `Depends(...)` in function signatures
- Declare dependencies as reusable `Annotated` type aliases
- Keep route handlers thin: delegate business logic to services, not routers
- Use Pydantic models for all request bodies and responses; avoid raw `dict`
- Raise `HTTPException` only at the router layer; services should raise domain exceptions

## Error Handling

- Distinguish between domain exceptions (raised in services) and HTTP exceptions (raised in routers)
- Never silence exceptions with bare `except:` or `except Exception: pass`
- Use specific exception types; avoid catching broad `Exception` unless re-raising

## Testing

- Use `pytest` with `pytest-asyncio` for async test support
- Prefer fixtures over setUp/tearDown patterns
- Each test should cover a single behavior; avoid testing multiple concerns in one test
- Use `task test` to fail fast on first error
