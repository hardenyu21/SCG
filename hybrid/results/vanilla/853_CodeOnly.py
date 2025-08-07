import os
import shutil
import string

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def task_func(directory_path):
    # Initialize summary dictionary
    summary = {}

    # Create the "Invalid" directory if it doesn't exist
    invalid_dir = os.path.join(directory_path, "Invalid")
    if not os.path.exists(invalid_dir):
        os.makedirs(invalid_dir)
        summary["Invalid"] = 0

    # Iterate over all files in the given directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check for invalid characters in the filename
        if any(char in INVALID_CHARACTERS for char in filename):
            # Move invalid files to the "Invalid" directory
            shutil.move(file_path, os.path.join(invalid_dir, filename))
            summary["Invalid"] += 1
            continue

        # Determine the file extension
        _, file_extension = os.path.splitext(filename)

        # Create a directory for the file extension if it doesn't exist
        extension_dir = os.path.join(directory_path, file_extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)
            summary[file_extension] = 0

        # Move the file to the corresponding extension directory
        shutil.move(file_path, os.path.join(extension_dir, filename))
        summary[file_extension] += 1

    return summary

# Example usage:
# summary = task_func('/path/to/directory')
# print(summary)