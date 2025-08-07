import re
from pathlib import Path
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Compile the regular expression pattern
    pattern = re.compile(file_pattern)
    
    # Create a Path object for the directory
    dir_path = Path(directory)
    
    # List to hold paths of files that match the pattern
    matching_files = []
    
    # Iterate over all files in the directory
    for file_path in dir_path.rglob('*'):
        # Check if the file path matches the pattern
        if pattern.search(str(file_path)):
            matching_files.append(file_path)
    
    # If no matching files are found, return None
    if not matching_files:
        return None
    
    # Create a tar file to archive the matching files
    tar_file_path = dir_path / 'archived_files.tar'
    with tarfile.open(tar_file_path, 'w') as tar:
        for file in matching_files:
            tar.add(file, arcname=file.relative_to(dir_path))
    
    # Return the path to the created tar file
    return str(tar_file_path)

# Example usage
# print(task_func())