"""
MCP Server for FastAPI Testing and Code Analysis
Provides tools for testing FastAPI endpoints and analyzing code
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


class MCPServer:
    """Local MCP Server for FastAPI project"""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.tools = {
            "run_tests": self.run_tests,
            "check_syntax": self.check_syntax,
            "start_server": self.start_server,
            "get_endpoints": self.get_endpoints,
            "analyze_models": self.analyze_models,
        }
    
    def run_tests(self, test_path: str = None) -> dict:
        """Run pytest tests"""
        try:
            cmd = ["python", "-m", "pytest", test_path or "tests/", "-v"]
            result = subprocess.run(cmd, cwd=self.project_root, capture_output=True, text=True)
            return {
                "status": "success" if result.returncode == 0 else "failed",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def check_syntax(self, file_path: str) -> dict:
        """Check Python file syntax"""
        try:
            cmd = ["python", "-m", "py_compile", file_path]
            result = subprocess.run(cmd, cwd=self.project_root, capture_output=True, text=True)
            return {
                "status": "valid" if result.returncode == 0 else "invalid",
                "message": result.stderr if result.stderr else "Syntax OK"
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def start_server(self, host: str = "127.0.0.1", port: int = 8000) -> dict:
        """Start FastAPI server"""
        try:
            cmd = ["uvicorn", "main:app", f"--host={host}", f"--port={port}", "--reload"]
            subprocess.Popen(cmd, cwd=self.project_root)
            return {
                "status": "started",
                "url": f"http://{host}:{port}",
                "docs": f"http://{host}:{port}/docs"
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_endpoints(self) -> dict:
        """List all FastAPI endpoints"""
        try:
            # Simple parsing of main.py for routes
            main_file = self.project_root / "main.py"
            if main_file.exists():
                content = main_file.read_text()
                endpoints = []
                for line in content.split('\n'):
                    if '@app.' in line:
                        endpoints.append(line.strip())
                return {"status": "success", "endpoints": endpoints}
            return {"status": "error", "message": "main.py not found"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def analyze_models(self) -> dict:
        """Analyze database models"""
        try:
            models_dir = self.project_root / "app" / "models"
            if models_dir.exists():
                models = []
                for py_file in models_dir.glob("*.py"):
                    if py_file.name != "__init__.py":
                        content = py_file.read_text()
                        if "class " in content:
                            models.append(py_file.name)
                return {"status": "success", "models": models}
            return {"status": "error", "message": "models directory not found"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def handle_request(self, method: str, params: dict = None) -> Any:
        """Handle MCP requests"""
        if method in self.tools:
            if params:
                return self.tools[method](**params)
            else:
                return self.tools[method]()
        return {"status": "error", "message": f"Unknown method: {method}"}


if __name__ == "__main__":
    project_root = Path(__file__).parent
    server = MCPServer(str(project_root))
    
    print("MCP Server initialized for FastAPI project")
    print("Available tools:")
    for tool in server.tools.keys():
        print(f"  - {tool}")
