import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    # Decode the base64-encoded JSON string
    decoded_bytes = base64.b64decode(raw_string)
    decoded_string = decoded_bytes.decode('utf-8')
    
    # Parse the JSON string into a Python dictionary
    data = json.loads(decoded_string)
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full file path
    file_path = os.path.join(output_dir, filename)
    
    # Write the data to a CSV file
    with open(file_path, mode='w', newline='') as csvfile:
        if data:
            # Use the keys of the first dictionary as the header
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header
            writer.writeheader()
            
            # Write the data rows
            for row in data:
                writer.writerow(row)
    
    # Return the path of the file
    return file_path
import unittest
import shutil
class TestCases(unittest.TestCase):
    def tearDown(self):
        if os.path.exists('./output'):
            shutil.rmtree('./output')
    
    def test_case_1(self):
        raw_string = 'eyJrZXkiOiAiVmFsdWUifQ=='
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,Value\n')
        os.remove(expected)
    
    def test_case_2(self):
        string_before = """{"key": "hello"}"""
        raw_string = base64.b64encode(string_before.encode('utf-8')).decode('utf-8')
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,hello\n')
        os.remove(expected)
    def test_case_3(self):
        string_before = """{"key": "hello", "key2": "world"}"""
        raw_string = base64.b64encode(string_before.encode('utf-8')).decode('utf-8')
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,hello\nkey2,world\n')
        os.remove(expected)
    def test_case_4(self):
        string_before = """{"key": "hello", "key2": "world", "key3": "!"}"""
        raw_string = base64.b64encode(string_before.encode('utf-8')).decode('utf-8')
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,hello\nkey2,world\nkey3,!\n')
        os.remove(expected)
    def test_case_5(self):
        string_before = """{"key": "hello", "key2": "world", "key3": "!", "key4": "test"}"""
        raw_string = base64.b64encode(string_before.encode('utf-8')).decode('utf-8')
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,hello\nkey2,world\nkey3,!\nkey4,test\n')
        os.remove(expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)