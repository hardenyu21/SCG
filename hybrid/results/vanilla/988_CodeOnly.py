import os
from pathlib import Path

def task_func(dir_path: str, predicates: list) -> dict:
    # Deduplicate predicates
    predicates = list(set(predicates))
    
    # Check if predicates are provided
    if not predicates:
        raise ValueError("No valid predicates are provided.")
    
    # Check if the specified directory exists and is a directory
    if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
        raise FileNotFoundError(f"The specified directory '{dir_path}' does not exist or is not a directory.")
    
    # Initialize the result dictionary
    result = {}
    
    # Iterate over each item in the directory
    for item in os.listdir(dir_path):
        # Evaluate each predicate against the item name
        item_result = [predicate(item) for predicate in predicates]
        
        # Store the results in the dictionary
        result[item] = item_result
    
    return result