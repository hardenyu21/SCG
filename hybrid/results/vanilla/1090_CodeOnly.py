import ast
import json
from collections import Counter

def task_func(file_pointer):
    # Load the JSON data from the file pointer
    data = json.load(file_pointer)
    
    # Initialize a Counter to keep track of key frequencies
    key_counter = Counter()
    
    # Iterate over each item in the JSON data
    for item in data:
        # If the item is a string, evaluate it to a dictionary
        if isinstance(item, str):
            try:
                item = ast.literal_eval(item)
            except (ValueError, SyntaxError):
                # If evaluation fails, skip this item
                continue
        
        # Ensure the item is a dictionary
        if isinstance(item, dict):
            # Update the counter with the keys from the dictionary
            key_counter.update(item.keys())
    
    return key_counter