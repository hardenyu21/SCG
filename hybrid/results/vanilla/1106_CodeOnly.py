from datetime import datetime
import os
from pathlib import Path

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(file_path):
    # Convert the file path to a Path object
    path = Path(file_path)
    
    # Check if the file exists
    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Get the creation time of the file
    creation_time = path.stat().st_ctime
    
    # Convert the creation time to a datetime object
    creation_datetime = datetime.fromtimestamp(creation_time)
    
    # Format the datetime object to the desired string format
    formatted_time = creation_datetime.strftime(DATE_FORMAT)
    
    return formatted_time