import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    joined_path = os.path.join(working_directory, file_path)
    full_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(joined_path)
    # print(joined_path)
    # print(full_working_directory)
    # print(full_file_path)

    if not full_file_path.startswith(full_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            added_msg = f'...File "{file_path}" truncated at 10000 characters'
            return file_content_string + added_msg
    except Exception as e:
        return f"Error during file reading: {e}"