# IBM Bob Agent Directives (AGENTS.md)

Welcome, IBM Bob. This document defines the product purpose, operational commands, and strict workflow rules governing autonomous operations within **PatchPilot-Python**.

---

## 🎯 Product Purpose

**PatchPilot-Python** is an autonomous code repair and evaluation platform powered by **IBM Bob**. Its mission is to ingest broken Python repositories, analyze the root cause of reported issues, synthesize localized reproduction tests, propose surgical patches, verify fixes against all test suites, and generate comprehensive audit reports.

---

## ⌨️ Essential Commands

| Command | Purpose |
| :--- | :--- |
| `streamlit run app.py` | Launch the PatchPilot interactive web dashboard |
| `python main.py --repo <path> --issue <path>` | Run the full CLI analysis, patch, and test cycle |
| `pytest sample_repository/test_app.py` | Run sample repository verification tests |
| `pytest tests/` | Execute PatchPilot-Python test suites |
| `python analyser.py <path>` | Perform standalone static/AST analysis of a repository |

---

## 📜 The 5 Strict Workflow Rules for IBM Bob

### Rule 1: Strict Red-to-Green Test Cycle
Before modifying any application source code, IBM Bob must always locate or construct a targeted reproduction test demonstrating the bug in a failing state (Red). A proposed patch is considered valid only when the reproduction test passes (Green) without causing regression.

### Rule 2: Minimal & Surgical Patching
Propose the most concise, targeted fix directly addressing the failure root cause. Do not refactor unrelated code, reformat files arbitrarily, or introduce speculative abstractions or unneeded dependencies.

### Rule 3: Comprehensive Regression Verification
Every patch must be verified by running the entire existing test suite in addition to the newly authored reproduction test. If any regression occurs, Bob must iterate or roll back immediately.

### Rule 4: Structured Auditing & Reporting
All actions, diagnostic hypotheses, code diffs, and test outcomes must be documented in a structured markdown report via `report.py` and persisted in `bob_sessions/`. Benchmark metrics must update `benchmark/evaluation-results.json`.

### Rule 5: Zero Secrets & Safe Environment Hygiene
Never write or log plain API keys, secrets, or tokens. Preserve all git history and branch integrity. Never perform destructive git commands (`git reset --hard`, unauthorized push, etc.) without explicit approval.
