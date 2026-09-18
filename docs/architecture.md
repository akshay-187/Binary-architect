# Architecture

This file is updated only when the design changes.

## Components

| Module | Responsibility |
|--------|-----------------|
| `app.py` | Streamlit UI: collects a bug report, displays plan/patch/report, and hosts the approval gates |
| `main.py` | CLI entry point for running the pipeline against a single issue file |
| `analyser.py` | Reads the issue and the target repository, produces a root-cause hypothesis |
| `ai_review.py` | Reviews a proposed patch before it is applied, using IBM Bob |
| `rules.py` | Loads and applies the guardrail rules from `.bob/rules/` at runtime |
| `report.py` | Assembles the final review-ready report from analysis, patch, and test results |
| `sample_repository/` | The target FastAPI app that PatchPilot analyses and patches — not part of PatchPilot itself |

## Workflow

```
Issue -> Analyse -> Plan -> [Approve] -> Patch -> Test -> Report -> [Approve]
```

The pipeline pauses at each `[Approve]` gate for human sign-off before
continuing to the next stage.
