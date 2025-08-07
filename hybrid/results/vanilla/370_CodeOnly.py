import os
import re
import json
import glob

def task_func(directory_path: str) -> list:
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(f"The specified directory '{directory_path}' does not exist.")
    
    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(directory_path, '*.json'))
    
    processed_files = []
    
    for file_path in json_files:
        # Read the content of the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Escape double quotes by prepending them with a double backslash
        escaped_content = content.replace('"', '\\"')
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(escaped_content)
        
        # Add the processed file to the list
        processed_files.append(file_path)
    
    return processed_files