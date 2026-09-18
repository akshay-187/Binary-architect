"""Unit tests for analyser.py in PatchPilot-Python."""

import pytest
from pathlib import Path
from analyser import RepoAnalyser


def test_repo_analyser_discovery(tmp_path):
    """Verifies that the RepoAnalyser correctly discovers Python files in a directory."""
    # Create sample python files in temporary directory
    sample_file = tmp_path / "sample.py"
    sample_file.write_text("def hello(): return 'world'\n", encoding="utf-8")

    analyser = RepoAnalyser(str(tmp_path))
    files = analyser.discover_python_files()

    assert len(files) == 1
    assert files[0].name == "sample.py"


def test_repo_analyser_ast_parsing(tmp_path):
    """Verifies that RepoAnalyser extracts function and class names via AST."""
    code = (
        "class Calculator:\n"
        "    def add(self, a, b):\n"
        "        return a + b\n\n"
        "def helper():\n"
        "    pass\n"
    )
    test_file = tmp_path / "calc.py"
    test_file.write_text(code, encoding="utf-8")

    analyser = RepoAnalyser(str(tmp_path))
    ast_info = analyser.parse_file_ast(test_file)

    assert ast_info["status"] == "parsed"
    assert "Calculator" in ast_info["classes"]
    assert "add" in ast_info["functions"]
    assert "helper" in ast_info["functions"]
