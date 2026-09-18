# Python Rules

- Target Python 3.11+.
- Use modern type hints (`str | None`, not `Optional[str]`).
- Format and lint with `ruff`.
- No mutable default arguments.
- No bare `except:` clauses.
- Keep functions under 40 lines.
- Import order: stdlib, then third-party, then local.
- No `print()` in library code — use logging instead.
