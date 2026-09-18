# Testing Rules

- Use `pytest`.
- Every bug fix gets a regression test: fails before the fix, passes after.
- Test names describe behavior, not implementation.
- One assertion per test where practical.
- Do not mock what you don't own.
- Run targeted tests before the full suite.
- Report failures honestly — never hide or soften them.
- Never skip a test to make a run look green.
