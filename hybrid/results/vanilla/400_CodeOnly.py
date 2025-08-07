import json
import os

def task_func(directory, string):
    def search_in_json(data, target_string):
        """Recursively search for a target string in a JSON data structure."""
        if isinstance(data, dict):
            for key, value in data.items():
                if search_in_json(value, target_string):
                    return True
        elif isinstance(data, list):
            for item in data:
                if search_in_json(item, target_string):
                    return True
        elif isinstance(data, str):
            return data == target_string
        return False

    def find_json_files(directory):
        """Recursively find all JSON files in a directory."""
        json_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.json'):
                    json_files.append(os.path.join(root, file))
        return json_files

    matching_files = []
    json_files = find_json_files(directory)

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if search_in_json(data, string):
                    matching_files.append(json_file)
        except (json.JSONDecodeError, IOError):
            # Skip files that cannot be read or are not valid JSON
            continue

    return matching_files