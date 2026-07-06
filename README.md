# Git Commit Linter — Golin

Golin is a lightweight git hook that validates your commit messages against the [Conventional Commits](https://www.conventionalcommits.org/) format before they're allowed into your repo. Bad commit messages like `fixed stuff` or `update` get blocked before they ever land in your history.

## Why

Six months from now, `git log` full of `fixed stuff` and `final version` tells you nothing. Golin forces every commit to say what it actually does, right from the moment it's written.

## Commit format

Every commit message must follow this pattern:

```
<type>: <description>
```

Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat: add login endpoint
fix: correct database query bug
docs: update setup instructions
```

Commits that don't follow this format are rejected with an error and a suggestion.

## Libraries used

1. `re` — for validating the commit message against the format
2. `sys` — for reading the commit message file path passed in by git

## How to use

1. Clone this repository:
   ```
   git clone https://github.com/Pranav-Pardeshii/git-commit-linter
   ```

2. Copy `linter.py` into the `.git/hooks/` folder of the repo you want to lint, renaming it to `commit-msg` (no file extension):
   ```
   Copy-Item linter.py .git/hooks/commit-msg -Force
   ```

3. Make sure the first line of `.git/hooks/commit-msg` (the shebang) matches your system:
   - **Windows:** `#!/usr/bin/env python`
   - **Mac/Linux:** `#!/usr/bin/env python3`


4. On Mac/Linux, make the hook executable:
   ```
   chmod +x .git/hooks/commit-msg
   ```
   (Not required on Windows.)

That's it — Golin now runs automatically every time you `git commit` in that repo.

## Example

```
$ git commit -m "fixed some stuff"
The commit message doesn't follow conventional commit message format!
eg. 'feat: implement commit message validator using regex'

$ git commit -m "feat: add commit message validation hook"
[main 3f2a1b9] feat: add commit message validation hook
```
