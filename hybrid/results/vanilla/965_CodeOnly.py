import os
import re
import shutil

def task_func(source_directory: str, target_directory: str, pattern: str = r"\d{4}") -> int:
    # Check if the source directory exists and is a directory
    if not os.path.isdir(source_directory):
        return 0

    # Create the target directory if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Compile the regex pattern
    regex = re.compile(pattern)

    # Initialize a counter for the number of files moved
    files_moved = 0

    # Iterate over all files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the filename matches the regex pattern
        if regex.search(filename):
            # Construct full file paths
            source_file = os.path.join(source_directory, filename)
            target_file = os.path.join(target_directory, filename)

            # Move the file
            shutil.move(source_file, target_file)
            files_moved += 1

    return files_moved