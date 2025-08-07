import os
import re
import shutil

# Constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def task_func():
    # Ensure the target directory exists
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # Iterate over all files in the source directory
    for filename in os.listdir(SOURCE_DIR):
        # Check if the file matches the pattern
        match = FILE_PATTERN.match(filename)
        if match:
            # Extract the prefix part of the filename
            prefix = match.group(1)
            # Construct the new filename
            new_filename = f"{prefix}.json"
            # Construct full file paths
            source_file = os.path.join(SOURCE_DIR, filename)
            target_file = os.path.join(TARGET_DIR, new_filename)
            # Move and rename the file
            shutil.move(source_file, target_file)

# Call the function to perform the task
task_func()