---
allowed-tools:
  - Bash(git branch --show-current)
  - Bash(git log *)
  - Bash(cat .github/PULL_REQUEST_TEMPLATE.md)
  - Bash(gh pr create *)
---

# Open Pull Request

Arguments: `$ARGUMENTS`

You are responsible for the **entire** PR creation flow. Execute all steps autonomously — only pause to ask the user when you face a genuine ambiguity that cannot be resolved from context.

---

## Step 1: Check the current branch

Run `git branch --show-current`.

If the current branch is `main`, warn the user that PRs must be opened from a feature branch and stop.

---

## Step 2: Gather context

Run in parallel:
- `git log main..HEAD --oneline` — list commits in this branch
- `git log main..HEAD --pretty=format:"%ae" | sort -u` — get unique author emails from signed commits
- `cat .github/PULL_REQUEST_TEMPLATE.md` — read the PR template

---

## Step 3: Infer PR fields

### Title
Derive from the branch name and commit list. Use the format:
```
<branch-name>: <short imperative description of the overall change>
```

### Scopes affected
Infer from the paths touched in the commits:

| Files | Scope |
|---|---|
| `backend/**` | Backend |
| `frontend/**` | Frontend |
| Both | Full Stack |
| `*.md`, `docs/**`, `.claude/**` | Documentation |

### Change checklist
Infer from the commits which items in the `## 🔍 Changes` section are applicable:

**Backend items:**
- `Services` — service layer files added or modified
- `Schemas` — `schemas/` files added or modified
- `Controller` — `controller/` files added or modified
- `Repository` — repository layer files added or modified
- `Core Config` — `core/` files added or modified
- `DevOps update (CI/CD)` — `.github/workflows/` files modified

**Frontend items:**
- `Pages` — page components added or modified
- `Components` — UI components added or modified
- `Hooks` — custom hooks added or modified
- `Lib Update` — lib/utility files modified
- `DevOps update (CI/CD)` — `.github/workflows/` files modified

### PR type checklist
Infer from the nature of the changes:

| Nature | Type |
|---|---|
| New functionality | Feature |
| Bug fix | Fix |
| Config, tooling, deps | Chore |
| CSS/styling only | Styling |
| Code restructure | Refactor |
| Tests added/updated | Test |

---

## Step 4: Fill the PR template

Use the `PULL_REQUEST_TEMPLATE.md` as the body. Fill each section:

- **What does this PR do?** — check the applicable type checkboxes
- **Scope** — check the applicable scope checkboxes
- **Description** — write a concise paragraph summarizing the intent of the PR
- **Changes** — check applicable items; **remove entirely the `### Backend` or `### Frontend` section if no files from that scope were changed**
- **How to test** — write numbered steps to manually verify the change (e.g. run commands, hit endpoints, check UI)
- **Notes** — add any relevant architectural decisions, tradeoffs, or gotchas; write `N/A` if none

### Assignee
Extract the author from the signed commits (`Co-Authored-By` lines or git log author email). Use `gh pr create --assignee @me` to assign the PR to the current user.

---

## Step 5: Create the PR

Run:
```bash
gh pr create \
  --base main \
  --title "<title>" \
  --assignee @me \
  --body "$(cat <<'EOF'
<filled template>
EOF
)"
```

Return the PR URL to the user.
