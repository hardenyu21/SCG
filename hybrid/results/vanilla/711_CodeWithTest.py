import json
import csv

def task_func(json_file, csv_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Check if the data is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON data must be a list of dictionaries.")
    
    # Write the data to a CSV file
    with open(csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        csv_writer = csv.DictWriter(file, fieldnames=data[0].keys())
        
        # Write the header
        csv_writer.writeheader()
        
        # Write the data rows
        for item in data:
            csv_writer.writerow(item)
    
    # Return the path to the CSV file
    return csv_file
import unittest
import os
class TestCases(unittest.TestCase):
    def tearDown(self):
        for file in ['./test.json', './test.csv', './testx.json', './testx.csv', './testy.json', './testy.csv', './testz.json', './testz.csv']:
            if os.path.exists(file):
                os.remove(file)
    def test_case_1(self):
        # Create json file
        json_file = './test.json'
        with open(json_file, 'w') as f:
            json.dump({'a': 1, 'b': 2, 'c': 3}, f)
        # Run function
        csv_file = task_func(json_file, './test.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['a', 'b', 'c'], ['1', '2', '3']])
        
    def test_case_2(self):
        # Create json file
        json_file = './test.json'
        with open(json_file, 'w') as f:
            json.dump({'z': 1, 'y': 2, 'x': 3}, f)
        # Run function
        csv_file = task_func(json_file, './test.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['z', 'y', 'x'], ['1', '2', '3']])
        
    def test_case_3(self):
        # Create json file
        json_file = './testx.json'
        with open(json_file, 'w') as f:
            json.dump({'xxx': 99}, f)
        # Run function
        csv_file = task_func(json_file, './testx.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['xxx'], ['99']])
        
    def test_case_4(self):
        # Create json file
        json_file = './testy.json'
        with open(json_file, 'w') as f:
            json.dump({'yyy': 99}, f)
        # Run function
        csv_file = task_func(json_file, './testy.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['yyy'], ['99']])
        
    def test_case_5(self):
        # Create json file
        json_file = './testz.json'
        with open(json_file, 'w') as f:
            json.dump({'zzz': 99}, f)
        # Run function
        csv_file = task_func(json_file, './testz.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['zzz'], ['99']])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)