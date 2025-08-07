import os
import re

def task_func(directory):
    BRACKET_PATTERN = r'[(){}[\]]'
    matched_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file name contains any bracket
            if re.search(BRACKET_PATTERN, file):
                # Construct the full file path
                file_path = os.path.join(root, file)
                matched_files.append(file_path)

    return matched_files

# Example usage:
# print(task_func('./another_directory/'))