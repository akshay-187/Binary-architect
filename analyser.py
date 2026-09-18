"""Repository Analyzer for PatchPilot-Python.
Inspects repository files, builds AST representations, and identifies failure points.
"""

import ast
import os
from pathlib import Path
from typing import Dict, List, Any


class RepoAnalyser:
    """Analyzes a Python repository structure, AST nodes, and test configurations."""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()

    def discover_python_files(self) -> List[Path]:
        """Finds all non-hidden Python source files in the repository."""
        if not self.repo_path.exists():
            return []
        return [
            p for p in self.repo_path.rglob("*.py")
            if not any(part.startswith(".") for part in p.parts)
        ]

    def parse_file_ast(self, file_path: Path) -> Dict[str, Any]:
        """Parses a Python file into an AST and extracts top-level functions and classes."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            tree = ast.parse(content, filename=str(file_path))
            classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            return {
                "file": str(file_path.relative_to(self.repo_path)),
                "classes": classes,
                "functions": functions,
                "status": "parsed",
            }
        except Exception as e:
            return {
                "file": str(file_path),
                "error": str(e),
                "status": "failed",
            }

    def analyze(self) -> Dict[str, Any]:
        """Executes a full repository analysis scan."""
        files = self.discover_python_files()
        parsed_files = [self.parse_file_ast(f) for f in files]
        return {
            "repo_path": str(self.repo_path),
            "total_python_files": len(files),
            "files": parsed_files,
        }


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "./sample_repository"
    analyser = RepoAnalyser(target)
    results = analyser.analyze()
    print(f"Discovered {results['total_python_files']} Python files in {target}")
    for item in results["files"]:
        print(f" - {item['file']}: {len(item.get('functions', []))} functions, {len(item.get('classes', []))} classes")
