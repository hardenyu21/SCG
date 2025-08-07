import json
import os

def task_func(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        return False
    
    try:
        # Open and load the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Check if the data is a list
        if not isinstance(data, list):
            return False
        
        # Check if each item in the list is a dictionary
        for item in data:
            if not isinstance(item, dict):
                return False
        
        return True
    
    except (json.JSONDecodeError, IOError):
        # Return False if there is an error reading the file or decoding JSON
        return False