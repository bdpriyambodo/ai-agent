import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    joined_path = os.path.join(working_directory, directory)
    # print(joined_path)

    # Normalize both paths (resolve "..", ".", etc.)
    full_path = os.path.abspath(joined_path)
    full_working_directory = os.path.abspath(working_directory)

    if not full_path.startswith(full_working_directory):
        # print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        # return
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        # print(f'Error: "{directory}" is not a directory')
        # return
        return f'Error: "{directory}" is not a directory'
    
    try:
        # print('full path: ' + full_path)
        # print('full working directory: ' + full_working_directory)
        dir_list = os.listdir(full_path)
        dir_fullpath_list = [(os.path.join(full_path,x)) for x in dir_list]
        size_list = [os.path.getsize(x) for x in dir_fullpath_list]
        checkdir_list = [os.path.isdir(x) for x in dir_fullpath_list]
        full_list = list(zip(dir_list,size_list,checkdir_list))
        string_list = [f"- {x[0]}: file_size={x[1]} bytes, is_dir={x[2]}" for x in full_list]
        combined_string = "\n".join(string_list)
        
        # print(dir_list)
        # print(dir_fullpath_list)
        # print(size_list)
        # print(file_list)
        # print(full_list)
        # print(string_list)
        # print(combined_string)
        return combined_string
    except Exception as e:
        return f"Error during listing and/or collecting directory/file info: {e}"






# get_files_info(".", "calculator")    
