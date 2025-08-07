import os
from pathlib import Path
import shutil

def task_func(source_directory: str, target_directory: str) -> int:
    # Define the valid file extensions
    valid_extensions = {'.txt', '.docx', '.xlsx', '.csv'}
    
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"The source directory '{source_directory}' does not exist.")
    
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)
    
    # Initialize a counter for the number of files moved
    files_moved = 0
    
    # Walk through the source directory recursively
    for root, _, files in os.walk(source_directory):
        for file in files:
            # Check if the file has a valid extension
            if Path(file).suffix in valid_extensions:
                # Construct the full path to the source file
                source_file_path = Path(root) / file
                
                # Construct the target file path
                target_file_path = Path(target_directory) / file
                
                # Handle naming conflicts by renaming duplicates
                if target_file_path.exists():
                    # Find a unique name for the file
                    base_name, extension = os.path.splitext(file)
                    counter = 1
                    while target_file_path.exists():
                        new_name = f"{base_name}-{counter}{extension}"
                        target_file_path = Path(target_directory) / new_name
                        counter += 1
                
                # Move the file to the target directory
                shutil.move(str(source_file_path), str(target_file_path))
                files_moved += 1
    
    return files_moved