# AGENTS.md

PatchPilot is an IBM Bob-powered issue-to-tested-patch workflow. It takes a bug
report describing an issue in a target repository and produces a root-cause
explanation, a minimal code patch, a regression test, a validation result, and
a review-ready report — passing through three human approval gates along the
way (plan approval, patch approval, report approval).

## Ground rules (READ FIRST)

1. Read `docs/PROJECT_MAP.md` before exploring the codebase.
2. Read `logs/session-state.md` before starting any new work.
3. Never modify files outside the current task's stated scope.
4. Never weaken, skip, or delete a test to make it pass.
5. Every bug fix ships with a regression test.
6. Update `logs/session-state.md` before ending a session.

## Repository map

| Path | Purpose |
|------|---------|
| `sample_repository/` | Target FastAPI app that Bob analyses and fixes |
| `app.py` | PatchPilot Streamlit UI entry point |
| `main.py` | PatchPilot CLI entry point |
| `analyser.py` | Issue analysis / root-cause logic |
| `ai_review.py` | AI-assisted review logic |
| `rules.py` | Rule definitions used by the pipeline |
| `report.py` | Review-ready report generation |
| `benchmark/` | Benchmark issues and evaluation results |
| `bob_sessions/` | Exported IBM Bob session reports |
| `docs/` | Project documentation |
| `logs/` | Session state and development log |

## Commands

| Command | Purpose |
|---------|---------|
| `streamlit run app.py` | Launch the PatchPilot UI |
| `pytest` | Run the test suite |
| `python main.py --issue <path>` | Run the pipeline against an issue file |

## Where to look

| Intent | File |
|--------|------|
| Architecture | `docs/ARCHITECTURE.md` |
| File locations | `docs/PROJECT_MAP.md` |
| Terminology | `docs/GLOSSARY.md` |
| Past decisions | `docs/DECISIONS.md` |
| Resume a session | `logs/session-state.md` |
| Style conventions | `docs/CONVENTIONS.md` |

## Rules and commands

Always-on guardrails live in `.bob/rules/`. Mode-specific rules live in
`.bob/rules-plan/`, `.bob/rules-code/`, and `.bob/rules-ask/`. Slash commands
live in `.bob/commands/`.
