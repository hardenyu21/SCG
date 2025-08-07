import sys
import subprocess

# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    try:
        # Check if the specified Python version is installed
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        current_version = result.stdout.strip().split()[1]
        
        if current_version != python_version:
            raise ValueError(f"Current Python version is {current_version}, but {python_version} is required.")
        
        # Append the specified path to sys.path if it's not already present
        if path_to_append not in sys.path:
            sys.path.append(path_to_append)
        
        return python_version
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    switched_version = task_func()
    if switched_version:
        print(f"Switched to Python version: {switched_version}")
    else:
        print("Failed to switch Python version.")