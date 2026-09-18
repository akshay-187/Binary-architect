# Project Map

Read this before exploring the codebase. It exists so Bob does not have to
grep blindly.

## Entry points

| File | Purpose |
|------|---------|
| `app.py` | PatchPilot Streamlit UI |
| `main.py` | PatchPilot CLI |
| `sample_repository/app.py` | Target FastAPI app under analysis |

## Core modules

| Module | Purpose | Key functions |
|--------|---------|----------------|
| `analyser.py` | Root-cause analysis of an issue | `analyse_issue`, `locate_fault` |
| `ai_review.py` | AI-assisted review of proposed patches | `review_patch` |
| `rules.py` | Rule definitions used across the pipeline | `load_rules`, `apply_rules` |
| `report.py` | Review-ready report generation | `build_report` |

## Data directories

| Path | Contents |
|------|----------|
| `benchmark/issues/` | Benchmark bug reports |
| `benchmark/evaluation-results.json` | Benchmark evaluation results |
| `bob_sessions/` | Exported IBM Bob session reports |

## Don't touch

- `.env` — never read, print, or modify.
- `bob_sessions/` — read-only unless actively exporting a session.
- `docs/DECISIONS.md` — append-only, never edit past entries.
