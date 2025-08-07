import collections
import json
import os

def task_func(directory_path: str) -> dict:
    def count_keys_in_json(file_path: str) -> dict:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return count_keys(data)

    def count_keys(data):
        if isinstance(data, dict):
            counter = collections.defaultdict(int)
            for key, value in data.items():
                counter[key] += 1
                counter.update(count_keys(value))
            return counter
        elif isinstance(data, list):
            counter = collections.defaultdict(int)
            for item in data:
                counter.update(count_keys(item))
            return counter
        else:
            return {}

    key_count = collections.defaultdict(int)
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                key_count.update(count_keys_in_json(file_path))

    return dict(key_count)