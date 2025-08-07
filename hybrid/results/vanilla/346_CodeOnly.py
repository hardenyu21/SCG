import subprocess
import os
import sys

def task_func(script_path, wait=True, *args):
    # Check if the script exists
    if not os.path.isfile(script_path):
        raise ValueError(f"The script '{script_path}' does not exist.")
    
    # Prepare the command to run the script with arguments
    command = [sys.executable, script_path] + list(args)
    
    try:
        # Start the subprocess
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if wait:
            # Wait for the process to complete and capture the output
            stdout, stderr = process.communicate()
            
            # Check if the process raised an exception
            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, command, output=stdout, stderr=stderr)
            
            # Return the return code
            return process.returncode
        else:
            # Return None if not waiting for the process to complete
            return None
    except subprocess.CalledProcessError as e:
        # Raise the exception if the script raises an exception
        raise subprocess.CalledProcessError(e.returncode, e.cmd, output=e.output, stderr=e.stderr)