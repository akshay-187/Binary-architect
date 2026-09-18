# PatchPilot-Python 🚀

> **IBM Bob-Powered Automated Code Repair & Benchmarking System**  
> *Developed by team Binary-architect*

---

## 📌 Overview

**PatchPilot-Python** is an automated software analysis and repair workflow driven by **IBM Bob**. It continuously monitors target Python repositories for issues, performs automated root-cause localization, generates targeted candidate patches, writes regression-proof tests, and produces audit-ready resolution reports.

---

## 🎯 Key Features

- **Automated Repository Analysis (`analyser.py`)**: Traverses the target codebase, detects syntax/logic bottlenecks, parses AST trees, and correlates issue statements with source files.
- **IBM Bob AI Review (`ai_review.py`)**: Integrates with IBM Bob / Granite model family to reason over failure modes, draft surgical patches, and synthesize reproduction tests.
- **Verification & Testing (`pytest`)**: Ensures code follows a strict red-to-green verification workflow by running reproduction and regression tests.
- **Interactive Streamlit Dashboard (`app.py`)**: Provides a real-time UI to visualize repository structure, view agent reasoning steps, inspect patch diffs, and review test results.
- **CLI Orchestration (`main.py`)**: Supports automated and headless execution suited for CI/CD pipelines and benchmark suites.
- **Comprehensive Reporting (`report.py`)**: Emits structured Markdown summaries capturing the issue description, root cause, patch diff, and verification status.

---

## 📁 Project Structure

```text
Binary-architect/
├── app.py                      # Streamlit UI Dashboard
├── main.py                     # CLI Orchestrator
├── analyser.py                 # Repository Analyzer & AST parser
├── ai_review.py                # IBM Bob integration & prompt engine
├── report.py                   # Markdown report generator
├── requirements.txt            # Project dependencies
├── .env.example                # Safe environment variables template
├── .gitignore                  # Standard Python ignore rules
├── README.md                   # Project description & setup guide
├── AGENTS.md                   # IBM Bob context, rules & commands
├── sample_repository/          # Seeded broken repository for testing
│   ├── app.py                  # FastAPI app with seeded empty phone bug
│   ├── requirements.txt        # Sample repo dependencies
│   └── test_app.py             # Pytest test file exposing the bug
├── benchmark/
│   ├── issues/
│   │   └── issue-01.md         # Problem description for seeded 500 error
│   └── evaluation-results.json # Metrics & evaluation tracking schema
├── .bob/
│   └── rules/
│       └── 01-workflow.md      # 5 strict workflow rules for Bob
├── bob_sessions/               # Runtime logs & generated session artifacts
│   └── .gitkeep
├── docs/
│   ├── architecture.md         # System architecture specification
│   └── demo-script.md          # Demonstration & presentation walkthrough
└── tests/
    └── test_analyser.py        # Unit tests for the analyzer module
```

---

## ⚙️ Quickstart

### 1. Installation

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env and supply your IBM Bob / Watsonx API credentials
```

### 3. Run the Streamlit UI

```bash
streamlit run app.py
```

### 4. Run via CLI Orchestrator

```bash
python main.py --repo ./sample_repository --issue ./benchmark/issues/issue-01.md
```

### 5. Run Tests

```bash
pytest tests/
pytest sample_repository/test_app.py
```
