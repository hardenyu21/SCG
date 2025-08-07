import shutil
import pathlib

def task_func(source_path, destination_path):
    # Convert paths to pathlib.Path objects
    source_path = pathlib.Path(source_path)
    destination_path = pathlib.Path(destination_path)
    
    # Check if source_path exists and is a directory
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError("source_path does not exist or is not a directory.")
    
    # Ensure destination_path exists, create if it doesn't
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # List files in the source directory without descending into subdirectories
    files_copied = []
    for item in source_path.iterdir():
        if item.is_file():
            # Copy the file to the destination directory
            shutil.copy(item, destination_path)
            # Append the filename to the list
            files_copied.append(item.name)
    
    # Return the source directory name and the list of copied filenames
    return (source_path.name, files_copied)