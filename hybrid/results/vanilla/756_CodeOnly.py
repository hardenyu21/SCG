import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    # Convert source_dir and target_dir to Path objects
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Check if source_dir and target_dir exist
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError(f"Source directory '{source_dir}' does not exist.")
    if not target_path.exists() or not target_path.is_dir():
        raise ValueError(f"Target directory '{target_dir}' does not exist.")
    
    # Initialize a counter for moved files
    moved_files_count = 0
    
    # Iterate over all files in the source directory
    for file in source_path.iterdir():
        # Check if the file has one of the specified extensions
        if file.is_file() and file.suffix in extensions:
            # Move the file to the target directory
            shutil.move(str(file), target_path / file.name)
            # Increment the counter
            moved_files_count += 1
    
    # Return the number of moved files
    return moved_files_count