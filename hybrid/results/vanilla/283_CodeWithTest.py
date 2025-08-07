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
import unittest
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.mock_data_directory = tempfile.mkdtemp()
        
        # Create mock data
        mock_data = [
            {'name': 'John', 'city': 'New York'},
            {'name': 'Jane', 'city': 'Los Angeles'},
            {'name': 'John', 'city': 'New York'},
            {'name': 'Alice', 'city': 'Chicago'},
            {'name': 'Bob', 'city': 'New York'},
            {'name': 'Alice', 'city': 'Chicago'},
            {'name': 'Alice', 'city': 'Chicago'},
            {'city': 'Los Angeles'},
            {'city': 'Chicago'},
            {'city': 'New York'},
            {'city': 'New York'},
            {'city': 'New York'},
        ]
        
        for i, data in enumerate(mock_data):
            with open(f"{self.mock_data_directory}/{i}.json", 'w') as file:
                json.dump(data, file)
    
    def test_case_1(self):
        # Test with mock data directory and 'name' key
        result = task_func(self.mock_data_directory, 'name')
        
        # To verify the result, we need to read all JSON files and count the occurrences of the 'name' key values
        expected_counts = []
        for filename in os.listdir(self.mock_data_directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.mock_data_directory, filename), 'r') as file:
                    data = json.load(file)
                    if 'name' in data:
                        expected_counts.append(data['name'])
                        
        expected_result = dict(Counter(expected_counts))
        
        self.assertDictEqual(result, expected_result)
    def test_case_2(self):
        # Test with a non-existent key
        result = task_func(self.mock_data_directory, 'non_existent_key')
        self.assertDictEqual(result, {})
    def test_case_3(self):
        # Test with another key present in our mock data ('city' in this case)
        result = task_func(self.mock_data_directory, 'city')
        
        # To verify the result, we need to read all JSON files and count the occurrences of the 'city' key values
        expected_counts = []
        for filename in os.listdir(self.mock_data_directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.mock_data_directory, filename), 'r') as file:
                    data = json.load(file)
                    if 'city' in data:
                        expected_counts.append(data['city'])
                        
        expected_result = dict(Counter(expected_counts))
        
        self.assertDictEqual(result, expected_result)
    def test_case_4(self):
        # Test with a directory that doesn't contain any JSON files
        empty_directory = f"{self.mock_data_directory}/empty_directory/"
        os.makedirs(empty_directory, exist_ok=True)
        
        result = task_func(empty_directory, 'name')
        self.assertDictEqual(result, {})
    def test_case_5(self):
        # Test with a directory that doesn't exist
        non_existent_directory = f"{self.mock_data_directory}/non_existent_directory/"
        
        with self.assertRaises(FileNotFoundError):
            task_func(non_existent_directory, 'name')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)