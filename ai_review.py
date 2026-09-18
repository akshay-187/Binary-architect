"""IBM Bob AI Integration Module for PatchPilot-Python.
Handles communication with IBM Bob / Watsonx API to analyze issues, propose patches, and write tests.
"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()


class IBMBobReviewer:
    """Interacts with IBM Bob / Watsonx Granite foundation models for code repair."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        project_id: Optional[str] = None,
        model_id: Optional[str] = None,
    ):
        self.api_key = api_key or os.getenv("IBM_BOB_API_KEY", "")
        self.project_id = project_id or os.getenv("IBM_BOB_PROJECT_ID", "")
        self.model_id = model_id or os.getenv("IBM_BOB_MODEL_ID", "ibm/granite-3-8b-instruct")

    def diagnose_issue(self, issue_description: str, repo_context: Dict[str, Any]) -> str:
        """Sends problem description and repo context to IBM Bob to determine root cause."""
        # Placeholder logic simulating model response or stubbing API client
        return (
            f"[IBM Bob Diagnosis] Analyzed issue against {repo_context.get('total_python_files', 0)} files. "
            "Identified missing input validation handling for empty string inputs in endpoint parameters."
        )

    def propose_patch(self, file_path: str, file_content: str, issue_summary: str) -> Dict[str, str]:
        """Prompts IBM Bob to generate a unified diff patch for the offending file."""
        return {
            "target_file": file_path,
            "patch_diff": (
                "--- a/sample_repository/app.py\n"
                "+++ b/sample_repository/app.py\n"
                "@@ -15,2 +15,4 @@\n"
                "+    if not user.phone or not user.phone.strip():\n"
                "+        raise HTTPException(status_code=400, detail='Phone number cannot be empty')\n"
            ),
            "explanation": "Added guard clause to validate non-empty phone number before formatting.",
        }

    def write_reproduction_test(self, issue_description: str) -> str:
        """Prompts IBM Bob to synthesize a pytest test reproducing the issue."""
        return (
            "def test_create_user_empty_phone_should_fail(client):\n"
            "    response = client.post('/users', json={'name': 'Alice', 'email': 'alice@example.com', 'phone': ''})\n"
            "    assert response.status_code == 400\n"
            "    assert response.json()['detail'] == 'Phone number cannot be empty'\n"
        )
