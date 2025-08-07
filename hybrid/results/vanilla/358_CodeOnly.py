import itertools
import json

def task_func(json_list, r):
    try:
        # Parse the JSON string
        data = json.loads(json_list)
        
        # Check if 'number_list' key exists
        if 'number_list' not in data:
            raise Exception("JSON data does not contain 'number_list' key.")
        
        # Extract the number list
        number_list = data['number_list']
        
        # Check if the number list is empty
        if not number_list:
            raise Exception("The 'number_list' is empty.")
        
        # Generate all combinations of r elements
        combinations = list(itertools.combinations(number_list, r))
        
        return combinations
    
    except json.JSONDecodeError:
        raise Exception("Invalid JSON input.")
    except Exception as e:
        raise e

# Example usage:
# json_input = '{"number_list": [1, 2, 3, 4]}'
# r = 2
# print(task_func(json_input, r))