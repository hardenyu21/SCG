import re
import json
import os

def task_func(file_path: str, regex_pattern=r'\(.+?\)|\w') -> dict:
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Extract the filename from the file path
    filename = os.path.basename(file_path)
    
    # Initialize a dictionary to store the results
    result = {filename: []}
    
    # Open and read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            # Load the JSON content
            json_content = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from file {file_path}: {e}")
    
    # Convert the JSON content to a string
    json_str = json.dumps(json_content)
    
    # Find all matches using the regular expression pattern
    matches = re.findall(regex_pattern, json_str)
    
    # Store the matches in the result dictionary
    result[filename] = matches
    
    return result