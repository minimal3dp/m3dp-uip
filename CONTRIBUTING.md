# Contributing to M3DP-UIP

Thanks for your interest in contributing! This project follows a phased build-out with an emphasis on:

1. CSV-driven, formula-accurate calculators
2. Router-based selective retrieval (avoid context pollution)
3. Clear separation of concerns (API / services / data)
4. Minimal, deterministic model prompts

## Workflow

1. Create a branch from `main` or `develop`: `feature/<short-description>`
2. Run tests locally: `pytest -q`
3. Format & lint: `ruff format . && ruff check . --fix`
4. Commit using Conventional Commits (e.g., `feat: add pressure advance calculator`)
5. Open a Pull Request with a concise description and any CSV row references for formulas.

## Adding a Calculator

1. Locate the source formula in the CSV or guide docs.
2. Implement pure math logic (no model calls) in a function under `backend/app/services/` or a new `calculators` module.
3. Add tests referencing sample input/output from the CSV.
4. Document usage in the README or dedicated docs page.

## Environment

Use UV for dependency management:

```bash
pip install uv
uv venv .venv
source .venv/bin/activate
uv pip install -e '.[dev]'
```

## Code Style

- Python 3.12+
- Ruff for lint + format
- 100 column line width
- Prefer explicit imports, avoid wildcard `*`

## Tests

- Place tests in `backend/tests/`.
- Use `pytest` & `pytest-asyncio` for async endpoints.
- Include coverage for new logic; skip heavy integration until necessary.

## Security

- Do not commit secrets; use `.env` for local.
- Never dump entire CSV datasets into prompts; rely on targeted retrieval.

## Discuss First

If unsure about an architectural change (e.g., adding a vector DB, new service layer, or third-party integration), open a GitHub Issue first.

## License

Contributions are under the MIT License.
