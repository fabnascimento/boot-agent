import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_file_path = os.path.abspath(full_path)
        abs_path_to_workdir = os.path.abspath(working_directory)

        is_file = os.path.isfile(abs_file_path)

        if not abs_file_path.startswith(abs_path_to_workdir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not is_file:
            f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path, 'r') as file:
            file_content = file.read()

            if(len(file_content) > MAX_CHARS):
                return f"{file_content[:MAX_CHARS]}\n[...File '{file_path}' truncated at {MAX_CHARS} characters]"

            return f"{file_content}"

    except Exception as e:
        return f"Error: {e}"