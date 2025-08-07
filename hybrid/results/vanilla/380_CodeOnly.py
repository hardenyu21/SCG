import re
import os
import shutil

def task_func(directory):
    # Check if the provided directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return None

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Construct full file path
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Extract file extension
        match = re.search(r'\.([a-zA-Z0-9]+)$', filename)
        if match:
            extension = match.group(1)
        else:
            # If no extension, skip the file
            continue
        
        # Create a directory for the extension if it doesn't exist
        extension_dir = os.path.join(directory, extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)
        
        # Move the file to the corresponding extension directory
        shutil.move(file_path, os.path.join(extension_dir, filename))

    return None