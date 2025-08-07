import os
import shutil

def task_func(path, delimiter="/"):
    # Validate the input path
    if not isinstance(path, str) or not path:
        raise ValueError("The 'path' must be a non-empty string.")
    
    # Split the path by the specified delimiter
    components = path.split(delimiter)
    
    # Check for invalid components
    if any(not component for component in components):
        raise ValueError("The 'path' contains invalid components.")
    
    # Initialize the result list
    result = []
    
    # Construct the full path for each component and calculate disk usage
    current_path = ""
    for component in components:
        if current_path:
            current_path = os.path.join(current_path, component)
        else:
            current_path = component
        
        # Check if the current path exists
        if not os.path.exists(current_path):
            raise FileNotFoundError(f"The path '{current_path}' does not exist in the filesystem.")
        
        # Get disk usage statistics
        total, used, free = shutil.disk_usage(current_path)
        
        # Append the component and its disk usage to the result list
        result.append((component, {'total': total, 'used': used, 'free': free}))
    
    return result