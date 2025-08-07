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
import unittest
import tempfile
import doctest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.json_file = tempfile.NamedTemporaryFile(delete=False)
    def tearDown(self):
        os.unlink(self.json_file.name)
    def test_case_1(self):
        data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value1'}
        result_path = task_func(data, self.json_file.name)
        self.assertTrue(os.path.exists(result_path), "JSON file doesn't exist.")
        with open(result_path, 'r') as f:
            json_data = json.load(f)
            self.assertEqual(json_data['data']['a'], 1)
            self.assertEqual(json_data['freq']['value1'], 2)
    
    def test_case_2(self):
        data = {}
        result_path = task_func(data, self.json_file.name)
        self.assertTrue(os.path.exists(result_path), "JSON file doesn't exist.")
        with open(result_path, 'r') as f:
            json_data = json.load(f)
            self.assertEqual(json_data['data']['a'], 1)
            self.assertEqual(json_data['freq']['1'], 1)
    
    def test_case_3(self):
        data = {'x': 'y', 'z': 'y'}
        result_path = task_func(data, self.json_file.name)
        self.assertTrue(os.path.exists(result_path), "JSON file doesn't exist.")
        with open(result_path, 'r') as f:
            json_data = json.load(f)
            self.assertEqual(json_data['data']['a'], 1)
            self.assertEqual(json_data['freq']['y'], 2)
            
    def test_case_4(self):
        data = {'e': 'b', 'c': 'd'}
        result_path = task_func(data, self.json_file.name)
        self.assertTrue(os.path.exists(result_path), "JSON file doesn't exist.")
        with open(result_path, 'r') as f:
            json_data = json.load(f)
            self.assertEqual(json_data['data']['a'], 1)
            self.assertEqual(json_data['freq']['b'], 1)
            
    def test_case_5(self):
        data = {'apple': 'fruit', 'carrot': 'vegetable'}
        result_path = task_func(data, self.json_file.name)
        self.assertTrue(os.path.exists(result_path), "JSON file doesn't exist.")
        with open(result_path, 'r') as f:
            json_data = json.load(f)
            self.assertEqual(json_data['data']['a'], 1)
            self.assertEqual(json_data['freq']['fruit'], 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)