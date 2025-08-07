import sys
from pathlib import Path

# Constants
PATH_TO_APPEND = '/path/to/whatever'

def task_func(path_to_append=PATH_TO_APPEND):
    # Append the path to sys.path if it's not already there
    if path_to_append not in sys.path:
        sys.path.append(path_to_append)
    
    # Create a Path object for the directory
    directory_path = Path(path_to_append)
    
    # Create the directory if it does not exist
    if not directory_path.exists():
        directory_path.mkdir(parents=True, exist_ok=True)
    
    # Output the path that was appended and where the directory was created
    return path_to_append

# Example usage
print(task_func())