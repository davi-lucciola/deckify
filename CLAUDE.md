# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Deckify is an open-source flashcard study platform with AI-assisted deck creation and community sharing. It's a monorepo with a Python/FastAPI backend and a Next.js frontend.

## Common Commands

### Backend (run from `/backend`)
```bash
uv sync                          # Install dependencies
task dev                         # Start dev server (uvicorn, port 8000)
task test                        # Run pytest with coverage (-s -x --cov=app -vv)
task format                      # Format with ruff
task lint                        # mypy + ruff check
uv run pytest -s -x --cov=app -vv -k "test_name"  # Run a single test
```

### Frontend (run from `/frontend`)
```bash
yarn install                     # Install dependencies
yarn dev                         # Start Next.js dev server (port 3000, Turbopack)
yarn build                       # Production build
yarn lint                        # ESLint
yarn format                      # ESLint --fix
```

### Docker (run from project root)
```bash
docker compose up --build        # Build and start all services (API :8000, Web :3000, DB :5432)
```

## Architecture

- **Backend** (`/backend`): FastAPI, Python 3.13+, async-first with asyncpg + SQLAlchemy 2.0 async sessions. Dependencies managed with Astral UV. Configuration via Pydantic Settings (`app/config.py`). DB sessions are injected via FastAPI `Depends` with a custom type alias `SQLAlchemy = Annotated[AsyncSession, Depends(get_db)]` in `app/dependencies.py`.
- **Frontend** (`/frontend`): Next.js 15 with App Router (RSC), React 19, TypeScript 5, Tailwind CSS v4 (OKLch color system), shadcn/ui components with CVA variants. Node 22, Yarn.
- **Database**: PostgreSQL (async via asyncpg), no migrations tool yet (Alembic not configured).

## Code Quality & CI

- **Backend**: ruff (line-length 88, single quotes, select rules: I/F/E/W/PL/PT), mypy strict mode, pytest with 90% coverage minimum enforced in CI.
- **Frontend**: ESLint 9 + Prettier, TypeScript strict mode. Path alias: `@/*` maps to `src/*`.
- CI runs on PRs to `main`, triggered by path changes (`backend/**` or `frontend/**`).

## Commit & Branch Conventions

Commit format: `[<scope>] <type>/<name>: <description>`
- Scopes: `backend`, `frontend`, `infra`, `docs`
- Types: `feat`, `bugfix`, `test`, `docs`, `infra`
- Example: `[backend] feat/deck-service: add create deck endpoint`

Branch naming: `feat/<name>`, `bugfix/<name>`, `docs/<name>`, `infra/<name>`

PRs target `main`. All tests, linting, and formatting must pass before merge.

@.claude/rules/python.md
