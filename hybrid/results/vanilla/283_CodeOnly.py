import os
import json
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    value_counts = Counter()
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    # Check if the key exists in the JSON data
                    if key in data:
                        value_counts[data[key]] += 1
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error reading {file_path}: {e}")
    
    return dict(value_counts)

# Example usage:
# result = task_func(json_files_path='./json_files/', key='product')
# print(result)