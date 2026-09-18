# Decisions

This log is append-only. Never edit or remove past entries.

## D-001: Python over Node

- Date: 2026-09-18
- Reason: Team velocity is higher in Python; Streamlit provides a fast UI
  path without a separate frontend build.
- Consequence: The whole PatchPilot stack (UI, pipeline, tests) is Python,
  simplifying tooling and onboarding for a 3-person, 48-hour team.

## D-002: FastAPI as target repo

- Date: 2026-09-18
- Reason: FastAPI apps are lightweight, easy to seed bugs into, and
  pytest-friendly, making them a good demo target for the hackathon.
- Consequence: `sample_repository/` is a small FastAPI app; PatchPilot's
  analysis and fix strategies are tuned first for that shape of codebase.
