import os

def task_func(path: str, delimiter: str = os.path.sep) -> list:
    # Convert backslashes to forward slashes
    path = path.replace('\\', '/')
    
    # Define invalid characters
    invalid_chars = set('<>:"|?*')
    
    # Check for invalid characters
    if any(char in invalid_chars for char in path):
        raise ValueError("The path contains invalid characters.")
    
    # Split the path into components using the specified delimiter
    components = path.split(delimiter)
    
    return components