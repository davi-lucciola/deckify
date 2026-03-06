# Commit Command

Execute the steps below in order to create a commit following the project conventions.

## Step 1: Check the current branch

Run `git branch --show-current`.

If the current branch is `main`:
- Warn the user that commits must not be made directly on `main`
- Inspect the staged/unstaged files (`git status`) to infer a branch name suggestion following the conventions:
  - `feat/<name>` for new features
  - `bugfix/<name>` for bug fixes
  - `docs/<name>` for documentation changes
  - `infra/<name>` for infrastructure or CI/CD changes
- Present the suggestion and ask the user to confirm or provide a different name
- Create and switch to the branch with `git checkout -b <branch-name>`

## Step 2: Check staged files

Run `git status` to inspect staged and unstaged changes.

If nothing is staged:
- Ask the user whether to stage all files (`git add .`) or specify which files to stage

## Step 3: Infer the scope

Based on the paths of staged files, infer the commit scope:

- Files under `backend/**` → scope `backend`
- Files under `frontend/**` → scope `frontend`
- Files under `.github/**`, `docker-compose*`, or other infra/CI files → scope `infra`
- Files matching `*.md` or under `docs/**` → scope `docs`
- Mixed changes spanning multiple scopes → ask the user which scope applies

## Step 4: Build the commit message

Ask the user for:
- **type**: one of `feat`, `bugfix`, `test`, `docs`, `infra`
- **name**: a short kebab-case identifier for the change (e.g. `deck-service`, `flashcard-ui`)
- **description**: a short imperative description of what the commit does

Then build the message in the format:
```
[<scope>] <type>/<name>: <description>
```

Example:
```
[backend] feat/deck-service: add create deck endpoint
```

## Step 5: Execute the commit

Run `git commit -m "<message>"` and show the result to the user.
