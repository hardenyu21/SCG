import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Split the input string into separate lines
    lines = input_string.splitlines()
    
    # Prepare a list to store file paths
    file_paths = []
    
    # Iterate over each line
    for i, line in enumerate(lines):
        # Remove special characters using regex
        cleaned_line = re.sub(f'[{re.escape(string.punctuation)}]', '', line)
        
        # Generate a random filename to avoid conflicts
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        filename = f"file_{i+1}_{random_suffix}.txt"
        file_path = os.path.join(directory, filename)
        
        # Write the cleaned line to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_line)
        
        # Add the file path to the list
        file_paths.append(file_path)
    
    return file_paths