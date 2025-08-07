import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        raise ValueError("The provided directory does not exist.")
    
    # Ensure the provided path is a directory
    if not os.path.isdir(directory_path):
        raise ValueError("The provided path is not a directory.")
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each entry in the directory
    for entry in os.scandir(directory_path):
        # Check if the entry is a file
        if entry.is_file():
            # Get the file name
            file_name = entry.name
            
            # Get the file size
            file_size = entry.stat().st_size
            
            # Get the creation time, if available, otherwise use the last metadata change time
            try:
                creation_time = datetime.fromtimestamp(entry.stat().st_ctime, tz=timezone.utc).isoformat()
            except AttributeError:
                creation_time = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
            
            # Get the last modification time
            modification_time = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
            
            # Append the tuple to the result list
            result.append((file_name, file_size, creation_time, modification_time))
    
    return result