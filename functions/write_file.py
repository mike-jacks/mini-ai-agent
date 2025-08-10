import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        }
    )
)

def write_file(working_directory, file_path, content):
    result = ""
    try:
        base_abs_path: str = os.path.abspath(working_directory)
        relative_file_path: str = os.path.join(working_directory, file_path)
        full_abs_file_path: str = os.path.abspath(relative_file_path)
        if not full_abs_file_path.startswith(base_abs_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        os.makedirs(os.path.dirname(full_abs_file_path), exist_ok=True)
        with open(full_abs_file_path, 'w') as file:
            file.write(content)
        result = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        return result
    except Exception as e:
        return f'Error: write_file failed: {e}'