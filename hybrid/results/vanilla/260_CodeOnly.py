import json
import os
import glob

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    # Find all JSON files in the specified directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    updated_count = 0

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Check if the key already exists
        if KEY not in data:
            data[KEY] = VALUE
            updated_count += 1

            # Write the updated data back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    return updated_count