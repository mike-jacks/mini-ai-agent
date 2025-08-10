import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of a file, constrained to the working directory. Returns the first 10,000 characters of the file and adds a warning if the file is truncated.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
    ),
)

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    result = ""
    try:
        base_abs_path = os.path.abspath(working_directory)
        relative_file_path = os.path.join(working_directory, file_path)
        full_abs_file_path = os.path.abspath(relative_file_path)
        if not full_abs_file_path.startswith(base_abs_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(relative_file_path):
            return f'Error: File not found or is not a regurlar file: "{file_path}"'
        if not os.path.exists(full_abs_file_path):
            return f'Error: File "{file_path}" not found.'
        with open(full_abs_file_path, 'r') as file:
            content = file.read(MAX_CHARS + 1)
            if len(content) > MAX_CHARS:
                content = content[:MAX_CHARS]
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        result = content
        return result
    except Exception as e:
        return f'Error: get_file_content failed: {e}'