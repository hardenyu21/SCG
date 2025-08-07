import os
from pathlib import Path
import shutil

def task_func(kwargs, target_dir="non_none_files"):
    # Ensure the target directory exists
    target_dir_path = Path(target_dir)
    target_dir_path.mkdir(parents=True, exist_ok=True)

    copied_files = []

    for file_name, file_path in kwargs.items():
        # Check if the file exists
        if Path(file_path).is_file():
            # Check if the file has content
            if os.path.getsize(file_path) > 0:
                # Define the destination path
                destination_path = target_dir_path / file_name
                # Copy the file to the target directory
                shutil.copy2(file_path, destination_path)
                # Add the copied file path to the list
                copied_files.append(str(destination_path))

    return copied_files