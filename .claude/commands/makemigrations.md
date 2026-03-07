---
allowed-tools:
  - Bash(find backend/migrations/versions -maxdepth 1 -name "*.py")
  - Bash(cd backend && DATABASE_URL=* uv run alembic revision --autogenerate -m *)
---

# Make Migration

Arguments: `$ARGUMENTS`

`$ARGUMENTS` is the migration description (e.g. `"create users table"`). If not provided, ask the user for a description before proceeding.

---

## Step 1: Determine the next migration number

Run:
```bash
find backend/migrations/versions -maxdepth 1 -name "*.py"
```

Count the number of `.py` files returned. The next migration number is `count + 1`, zero-padded to 4 digits (e.g. `0001`, `0002`).

---

## Step 2: Generate the migration

Run from the project root:
```bash
cd backend && DATABASE_URL="postgresql+asyncpg://admin:admin@localhost:5432/deckify" uv run alembic revision --autogenerate -m "<NEXT> $ARGUMENTS"
```

Where `<NEXT>` is the number calculated in Step 1.

---

## Step 3: Confirm

Show the user the name of the generated file and its `upgrade()` and `downgrade()` contents so they can verify the migration is correct.
