# PatchPilot-Python Demonstration Script 🎬

## Objective
Demonstrate an automated, end-to-end bug resolution cycle using PatchPilot-Python and IBM Bob against a real seeded bug in a FastAPI service.

---

## ⏱️ Timeline & Presentation Flow

### 1. The Challenge (0:00 - 0:30)
- Present `sample_repository/app.py`: A FastAPI endpoint `/users` that accepts user registrations.
- Show `benchmark/issues/issue-01.md`: A user submits an empty phone string, causing an unhandled `ValueError` and a `500 Internal Server Error`.

### 2. Live Reproduction (0:30 - 1:00)
- Run `pytest sample_repository/test_app.py`.
- Highlight the test failure: `test_create_user_with_empty_phone_should_return_400` fails with `500 != 400` (Red State).

### 3. Launching PatchPilot-Python (1:00 - 2:00)
- Launch the Streamlit dashboard: `streamlit run app.py` (or execute via `python main.py`).
- Show IBM Bob analyzing `sample_repository/`, identifying the missing validation guard in `create_user()`, and synthesizing a surgical patch.

### 4. Verification & Green State (2:00 - 3:00)
- Review the proposed patch diff.
- Run tests again: Reproduction test passes with HTTP 400, and health/valid user tests continue to pass (Green State).

### 5. Audit & Reporting (3:00 - 3:30)
- Inspect the generated markdown report in `bob_sessions/reports/` and metric updates in `benchmark/evaluation-results.json`.
