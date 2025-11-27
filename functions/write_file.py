import os

def write_file(working_directory, file_path, content):
    joined_path = os.path.join(working_directory, file_path)
    full_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(joined_path)

    if not full_file_path.startswith(full_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if os.path.exists(full_file_path):
            with open(full_file_path, "w") as f:
                f.write(content)
        else:
            dir_path = os.path.dirname(full_file_path)
            os.makedirs(dir_path, exist_ok = True)
            with open(full_file_path, "w") as f:
                f.write(content)
    except Exception as e:
        return f"Error during file writing: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'