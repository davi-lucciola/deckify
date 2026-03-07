---
allowed-tools:
  - Bash(git branch --show-current)
  - Bash(git status)
  - Bash(git add .)
  - Bash(git diff --staged)
  - Bash(git checkout -b *)
  - Bash(git commit -m *)
  - Bash(git push -u origin *)
---

# Commit and Push

Arguments: `$ARGUMENTS`

You are responsible for the **entire** commit and push flow. Execute all steps autonomously — only pause to ask the user when you face a genuine ambiguity that cannot be resolved from context.

If `$ARGUMENTS` contains `push`, perform all steps including Step 6 (push). Otherwise, stop after Step 5 (commit) and skip the push.

---

## Step 1: Check the current branch

Run `git branch --show-current`.

If the current branch is `main`:
- Warn the user that direct commits to `main` are not allowed
- Run `git status` to inspect changes and infer a branch name following the conventions:
  - `feat/<name>` — new features
  - `bugfix/<name>` — bug fixes
  - `docs/<name>` — documentation
  - `chore/<name>` — maintenance, config, tooling, dependencies
  - `infra/<name>` — infrastructure or CI/CD
- Suggest the branch name and ask the user to confirm or provide a different one
- Create and switch with `git checkout -b <branch-name>`

---

## Step 2: Stage files

Run `git status` to inspect staged and unstaged changes.

If nothing is staged, run `git add .` to stage all changes automatically.

---

## Step 3: Infer the commit fields

Run `git diff --staged` to understand what changed.

### Scope
Infer from the paths of staged files:

| Files | Scope |
|---|---|
| `backend/**` | `backend` |
| `frontend/**` | `frontend` |
| `.github/**`, `docker-compose*` | `infra` |
| `*.md`, `docs/**`, `.claude/**` | `docs` |
| Mixed across multiple scopes | ask the user |

### Type
Infer from the nature of the changes:

| Nature | Type |
|---|---|
| New functionality or endpoint | `feat` |
| Bug fix | `bugfix` |
| Tests added or updated | `test` |
| Documentation, rules, README | `docs` |
| Config, tooling, dependencies, formatting | `chore` |
| CI/CD, Docker, infra changes | `infra` |

### Name
Derive a short kebab-case identifier from the files or feature changed (e.g. `claude-rules`, `deck-service`, `biome-config`).

### Description
Write a short, imperative sentence describing what the commit does (e.g. `add typescript rules`, `fix login redirect`).

---

## Step 4: Build the commit message

Use the format:
```
[<scope>] <type>/<name>: <description>
```

Example:
```
[docs] chore/claude-rules: add typescript and python lint rules
```

---

## Step 5: Commit

Run:
```bash
git commit -m "[<scope>] <type>/<name>: <description>"
```

If the commit fails due to a pre-commit hook, fix the reported issue, re-stage, and create a **new** commit (never amend).

---

## Step 6: Push _(only if `$ARGUMENTS` contains `push`)_

Run:
```bash
git push -u origin <branch>
```

Show the result and confirm to the user that the branch has been pushed.
