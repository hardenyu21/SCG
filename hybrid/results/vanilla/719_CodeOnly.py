import re
import os
import glob

def task_func(directory, word):
    count = 0
    # Use glob to find all files in the directory
    for file_path in glob.glob(os.path.join(directory, '*')):
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            try:
                # Open the file and read its contents
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    # Use regular expression to find the word
                    if re.search(r'\b' + re.escape(word) + r'\b', content, re.IGNORECASE):
                        count += 1
            except Exception as e:
                # Handle any exceptions that occur while reading the file
                print(f"Error reading {file_path}: {e}")
    return count