import os
import sys
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="An argument to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        }
    )
)

def run_python_file(working_directory, file_path, args=None):
    if args is None:
        args = []
    try:
        base_abs_path: str = os.path.abspath(working_directory)
        relative_file_path: str = os.path.join(working_directory, file_path)
        full_abs_file_path: str = os.path.abspath(relative_file_path)
        if not full_abs_file_path.startswith(base_abs_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_abs_file_path):
            return f'Error: File "{file_path}" not found.'
        if not full_abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        completed = subprocess.run(
            [sys.executable, full_abs_file_path, *map(str, args)],
            capture_output=True,
            text=True,
            cwd=base_abs_path,
            timeout=30,
        )

        stdout_text = completed.stdout or ""
        stderr_text = completed.stderr or ""

        if stdout_text == "" and stderr_text == "":
            return "No output produced."
        
        parts = []
        if stdout_text != "":
            parts.append(f"STDOUT:\n{stdout_text}")
        if stderr_text != "":
            parts.append(f"STDERR:\n{stderr_text}")

        if completed.returncode != 0:
            parts.append(f"\nProcess exited with code {completed.returncode}")
        return "\n".join(parts)
    except Exception as e:
        return f'Error: executing Python file: {e}'