# /plan-issue

Loads `docs/PROJECT_MAP.md`, `logs/session-state.md`, and the relevant target
files, then produces a plan for the issue described in `$ARGUMENTS`.

No edits are made in this command.

## Output format

1. Reproduction path.
2. Relevant files (max 5, paths only).
3. Root-cause hypothesis.
4. Minimal fix, described in prose — no code.
5. Regression-test strategy.
6. Risks.
7. Validation commands to run afterward.

End with: "Reply APPROVE to proceed, or REVISE to adjust."
