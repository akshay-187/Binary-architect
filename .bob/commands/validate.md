# /validate

Runs, in order:

1. Targeted tests for the changed files.
2. The full `pytest` suite.
3. `ruff` lint.

Reports raw output for each step — no summarizing. Flags any skipped test
explicitly.
