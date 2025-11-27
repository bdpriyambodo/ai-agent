
import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    joined_path = os.path.join(working_directory, file_path)
    full_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(joined_path)

    if not full_file_path.startswith(full_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cmds = ['python', f'{full_file_path}']

        if args:
            cmds.extend(args)

        result = subprocess.run(
            cmds,
            cwd=full_working_directory,
            capture_output=True, 
            check=True,  # Raise CalledProcessError if the command returns a non-zero exit code
            text=True,    # Decode stdout and stderr as text using default encoding
            timeout=30, 
        )

        output = []
        
        return (f'STDOUT: {result.stdout} \nSTDERR: {result.stderr}')
        # print("Stdout:", result.stdout)
        # print("Stderr:", result.stderr)

    except subprocess.CalledProcessError as e:
        return(f'Process exited with code: {e}')
        # print("Command failed with error:", e)
        # print(f"Command failed with exit code {e.returncode}")
        # print("STDOUT:")
        # print(e.stdout)
        # print("STDERR:")
        # print(e.stderr)
    except Exception as e:
        return (f"Error: executing Python file: {e}")
