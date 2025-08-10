import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    result = ""
    try:
        base_abs_path = os.path.abspath(working_directory)
        relative_path = os.path.join(working_directory, directory)
        full_abs_path = os.path.abspath(relative_path)
        if not full_abs_path.startswith(base_abs_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(relative_path):
            return f'Error: "{relative_path}" is not a directory'
        contents = os.listdir(full_abs_path)
        if directory == ".":
            directory = "current"
        else:
            directory = f"'{directory}'"
        result += f'Result for {directory} directory:\n'
        for i in range(len(contents)):
            if contents[i] == "__pycache__":
                continue
            full_path_content = os.path.join(full_abs_path, contents[i])
            result += f' - {contents[i]}: file_size={os.path.getsize(full_path_content)} bytes, is_dir={os.path.isdir(full_path_content)}\n'
        return result
    except Exception as e:
        return f'Error: get_files_info failed: {e}'
        
