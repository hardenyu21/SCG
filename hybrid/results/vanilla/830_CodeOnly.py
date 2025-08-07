import json
import os

def task_func(filename, data):
    try:
        # Write the dictionary to a file as a JSON object
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        
        # Read the content back to verify
        with open(filename, 'r') as file:
            written_data = json.load(file)
        
        # Check if the file exists
        file_exists = os.path.exists(filename)
        
        # Return the result as a tuple and a boolean
        return (file_exists, written_data), file_exists, written_data
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return (False, None), False, None

# Example usage:
# result, success, written_data = task_func('example.json', {'key': 'value'})
# print(result, success, written_data)