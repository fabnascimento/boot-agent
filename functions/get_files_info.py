import os

CURRENT_DIR = "."

def get_files_info(working_directory, directory=CURRENT_DIR):
    try:
        full_path = os.path.join(working_directory, directory)
        abs_path = os.path.abspath(full_path)
        abs_path_to_workdir = os.path.abspath(working_directory)

        if not abs_path.startswith(abs_path_to_workdir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_path):
            return f'Error: "{directory}" is not a directory'

        contents = os.listdir(abs_path)
        content_map = {}

        for content in contents:
            content_path = os.path.join(abs_path, content)
            is_dir = os.path.isdir(content_path)
            size = os.path.getsize(content_path)

            content_map[content] = {
                "size": size,
                "is_dir": is_dir,
            }

        dir_display_name = directory if CURRENT_DIR != directory else 'current'
        header = f"Result for '{dir_display_name}'"
        format_body = lambda d: '\n'.join(
            f" - {k}: file_size={v['size']} bytes, is_dir={v['is_dir']}" for k, v in d.items()
        )

        return f"{header}\n{format_body(content_map)}"

    except Exception as e:
        return f'Error: {e}'
