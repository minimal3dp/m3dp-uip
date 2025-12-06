---
description: Code Quality Enforcer. Uses 'ruff' to lint and format the project.
---

1. Run Lint Check:
   - `ruff check .`
2. Report results. If errors exist, ask user for permission to fix.
3. Fix & Format (if approved):
   // turbo
   - `ruff check --fix .`
   - `ruff format .`
