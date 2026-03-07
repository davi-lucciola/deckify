---
name: makemigrations
description: >
  Use whenever the user wants to create or generate a new Alembic database
  migration in the Deckify backend. Trigger on phrases like "make migration",
  "create migration", "gerar migration", "nova migration", "alembic revision",
  or when the user adds/changes a SQLAlchemy model and needs to reflect it in
  the database schema. Only applies to the backend context — if the user is
  working on the frontend, warn them this skill is backend-only.
---

# Make Migration

Generates a new numbered Alembic migration file for the Deckify backend.

## Context check

This skill only applies to the **backend**. If the user appears to be working
outside the backend context (e.g., frontend-only changes), warn them:
> "The `makemigrations` skill only applies to the backend. Are you sure you
> want to generate a migration?"

## Available backend commands (from `pyproject.toml`)

| Command | Description |
|---|---|
| `task migrate` | Apply all pending migrations (`alembic upgrade head`) |
| `task format` | Format code with ruff |

---

## Step 1: Get the migration description

`$ARGUMENTS` is the migration description (e.g. `"create users table"`).

If not provided, ask the user before proceeding:
> "What should the migration be called? (e.g. `add users table`)"

---

## Step 2: Determine the next migration number

Run from the project root:
```bash
find backend/migrations/versions -maxdepth 1 -name "*.py"
```

Count the `.py` files returned. The next migration number is `count + 1`,
zero-padded to 4 digits (e.g. `0001`, `0002`, `0003`).

---

## Step 3: Generate the migration

Run from the project root:
```bash
cd backend && DATABASE_URL="postgresql+asyncpg://admin:admin@localhost:5432/deckify" uv run alembic revision --autogenerate -m "<NEXT> <DESCRIPTION>"
```

Where `<NEXT>` is the number from Step 2 and `<DESCRIPTION>` is the user's description.

---

## Step 4: Confirm

Show the user:
- The generated file name
- The contents of `upgrade()` and `downgrade()` so they can verify the schema change is correct

Then remind them:
> "To apply this migration, run `task migrate` from the `backend/` directory."
