import pandas as pd
import json

def task_func(file_path, key):
    # Load the JSON file into a list of dictionaries
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Remove the specified key from each dictionary
    for item in data:
        if key in item:
            del item[key]
    
    # Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(data)
    
    # Write the processed DataFrame back into a JSON file oriented by records
    df.to_json(file_path, orient='records', lines=True)
    
    # Return the DataFrame
    return df
import unittest
import os
class TestCases(unittest.TestCase):
    def base(self, json_path, key, contents):
        # Create JSON file
        with open(json_path, 'w') as file:
            json.dump(contents, file)
        # Run function
        df = task_func(json_path, key)
        # Check key is removed
        self.assertFalse(key in df.columns)
        # Check JSON file is updated
        with open(json_path, 'r') as file:
            data = json.load(file)
        self.assertFalse(key in data[0])
        # Remove JSON file
        os.remove(json_path)
    def test_case_1(self):
        self.base('data.json', 'ele', [{'ele': 1, 'a': 2}, {'ele': 3, 'a': 4}])
    def test_case_2(self):
        self.base('data.json', 'ele', [{'ele': 1, 'a': 2}, {'ele': 3, 'a': 4}, {'ele': 5, 'a': 6}])
    def test_case_3(self):
        self.base('x.json', 'zzz', [{'zzz': 1, 'a': 2}, {'zzz': 3, 'a': 4}])
    def test_case_4(self):
        self.base('g.json', 'ele', [{'ele': 1, 'a': 2}, {'ele': 3, 'a': 4}])
    def test_case_5(self):
        self.base('data.json', 'ele', [{'ele': 1, 'a': 2}, {'ele': 3, 'a': 4}])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)