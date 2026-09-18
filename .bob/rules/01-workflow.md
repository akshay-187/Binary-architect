# IBM Bob Strict Workflow Rules (01-workflow.md)

As an autonomous code repair agent operating under **PatchPilot-Python**, you must strictly adhere to the following 5 rules. No exceptions are permitted.

---

### Rule 1: Red-to-Green Pre-Condition
Never apply or propose modifications to application source files until a reproducing test has been identified or authored that cleanly reproduces the reported defect (Red status). Your patch is successful only when that reproduction test turns Green without regressions.

### Rule 2: Minimal & Surgical Edits
Write the minimal code change necessary to fix the defect. Do not refactor surrounding code, rewrite unrelated functions, adjust cosmetic formatting, or introduce new external dependencies unless explicitly instructed.

### Rule 3: Comprehensive Regression Testing
After drafting a patch, run both the reproduction test and the complete existing repository test suite. Any failure across the existing test suite constitutes an immediate regression and requires discarding or revising the patch candidate.

### Rule 4: Structured Reporting & Metric Export
Every repair session must produce a self-contained Markdown report following the template defined in `report.py`. The report must detail the root cause analysis, file diffs, and test assertions. Benchmark performance metrics must be recorded in `benchmark/evaluation-results.json`.

### Rule 5: Zero Secrets & Git Hygiene
Never print, store, or commit real API keys, environment tokens, or credentials. Respect `.gitignore` rules. Do not execute destructive git commands (`git reset --hard`, force push, deleting branches) without human review.
