import collections
import json
import os

def task_func(data, json_file_name='data.json'):
    # Add a new key "a" with the value 1 to the input dictionary
    data['a'] = 1
    
    # Calculate the frequency of the values in the dictionary
    value_counts = collections.Counter(data.values())
    
    # Create a dictionary to hold the data and its frequency distribution
    result = {
        'data': data,
        'freq': dict(value_counts)
    }
    
    # Write the result to a JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(result, json_file, indent=4)
    
    # Return the path of the JSON file
    return os.path.abspath(json_file_name)