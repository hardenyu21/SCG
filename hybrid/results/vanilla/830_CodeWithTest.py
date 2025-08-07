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
import unittest
import os
import json
from faker import Faker
fake = Faker()
class TestCases(unittest.TestCase):
    def setUp(self):
        """Create the test file with initial data."""
        self.filename = 'data.json'
        self.data = {'key': 'value'}
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
    def tearDown(self):
        """Remove the test file after all tests."""
        os.remove(self.filename)
    def test_empty_dict(self):
        """Test with an empty dictionary to ensure it writes and verifies correctly."""
        filename = 'empty_test.json'
        data = {}
        success, content = task_func(filename, data)
        self.assertTrue(success)
        self.assertEqual(content, data)
        os.remove(filename)
    def test_simple_dict(self):
        """Test with a simple dictionary to check for basic write and verify functionality."""
        filename = 'simple_test.json'
        data = {'key': 'value'}
        success, content = task_func(filename, data)
        self.assertTrue(success)
        self.assertEqual(content, data)
        os.remove(filename)
    def test_nested_dict(self):
        """Test with a nested dictionary to ensure nested structures are handled correctly."""
        filename = 'nested_test.json'
        data = {'key': {'nested_key': 'nested_value'}}
        success, content = task_func(filename, data)
        self.assertTrue(success)
        self.assertEqual(content, data)
        os.remove(filename)
    def test_large_dict(self):
        """Test with a large dictionary to ensure the function can handle more substantial amounts of data."""
        filename = 'large_test.json'
        data = {fake.word(): fake.sentence() for _ in range(100)}
        success, content = task_func(filename, data)
        self.assertTrue(success)
        self.assertEqual(content, data)
        os.remove(filename)
    def test_dict_with_various_types(self):
        """Test with a dictionary containing various data types to verify type handling."""
        filename = 'various_types_test.json'
        data = {
            'string': 'value',
            'number': 42,
            'float': 3.14,
            'bool': True,
            'none': None,
            'list': [1, 2, 3],
            'dict': {'nested': 'dict'}
        }
        success, content = task_func(filename, data)
        self.assertTrue(success)
        self.assertEqual(content, data)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)