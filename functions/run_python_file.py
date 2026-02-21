import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_file_abs = os.path.abspath(working_directory)

        target_file = os.path.normpath(os.path.join(working_file_abs, file_path))

        valid_target_file = os.path.commonpath([working_file_abs, target_file]) == working_file_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args:
            command.extend(args)

        completedprocess = subprocess.run(
            command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30)
        
        output = ""
        if completedprocess.returncode != 0:
            output += f"Process exited with code {completedprocess.returncode}"
        
        if completedprocess.stdout == "" and completedprocess.stderr == "":
            output += "No output produced"
        else:
            output += f"STDOUT: {completedprocess.stdout} STDERR: {completedprocess.stderr}"
        
        return output
    except Exception as e:
        return f"ERROR: {e}"
    