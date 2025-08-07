import re
import os
import glob
from pathlib import Path

def task_func(pattern, directory, extensions):
    # Compile the regex pattern with case insensitive flag
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Initialize a list to store the paths of files containing the pattern
    matching_files = []
    
    # Iterate over each specified extension
    for ext in extensions:
        # Use glob to find all files with the current extension in the directory
        search_pattern = os.path.join(directory, f'*.{ext}')
        for file_path in glob.glob(search_pattern):
            # Open and read the file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                # Check if the pattern is found in the file content
                if regex.search(content):
                    # Append the absolute path of the file to the list
                    matching_files.append(os.path.abspath(file_path))
    
    return matching_files