"""Markdown Report Generator for PatchPilot-Python.
Formats resolution summaries, patch diffs, test results, and metrics into clean Markdown.
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class ReportGenerator:
    """Generates structured Markdown reports for bug fixes and evaluation results."""

    def __init__(self, output_dir: str = "./bob_sessions/reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(
        self,
        issue_id: str,
        issue_title: str,
        diagnosis: str,
        patch_info: Dict[str, str],
        test_results: Dict[str, Any],
        filename: Optional[str] = None,
    ) -> Path:
        """Assembles a markdown report and writes it to disk."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_name = filename or f"patch_report_{issue_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_path = self.output_dir / report_name

        content = f"""# 🛡️ PatchPilot Resolution Report: {issue_id}

> **Generated on:** {timestamp}  
> **Engine:** IBM Bob Autonomous Code Repair

---

## 📌 Issue Summary
**Issue ID:** `{issue_id}`  
**Title:** {issue_title}  

---

## 🔍 Root Cause Analysis & Diagnosis
{diagnosis}

---

## 🩹 Proposed Patch
**Target File:** `{patch_info.get('target_file', 'unknown')}`  
**Explanation:** {patch_info.get('explanation', 'N/A')}  

```diff
{patch_info.get('patch_diff', '# No diff provided')}
```

---

## 🧪 Verification & Test Results
- **Reproduction Test Status:** `{'PASSED (Green)' if test_results.get('reproduction_passed') else 'FAILED (Red)'}`
- **Regression Suite Status:** `{'PASSED' if test_results.get('regression_passed') else 'FAILED'}`
- **Total Tests Executed:** `{test_results.get('total_tests', 1)}`

---

## 📈 Next Steps
- Review diff and merge PR.
- Update benchmark metrics in `benchmark/evaluation-results.json`.
"""

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(content)

        return report_path
