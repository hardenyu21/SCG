import json
import base64
import unicodedata

def task_func(json_file: str) -> dict:
    # Open and read the JSON file
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Initialize an empty dictionary to store the results
    result = {}
    
    # Iterate over each key-value pair in the JSON data
    for key, encoded_value in data.items():
        # Decode the base64 encoded string
        decoded_bytes = base64.b64decode(encoded_value)
        # Convert bytes to a UTF-8 string
        decoded_string = decoded_bytes.decode('utf-8')
        # Apply Unicode normalization form C (NFC)
        normalized_string = unicodedata.normalize('NFC', decoded_string)
        # Store the normalized string in the result dictionary
        result[key] = normalized_string
    
    return result
import unittest
from unittest.mock import mock_open, patch
import json
class TestCases(unittest.TestCase):
    def setUp(self):
        # Initialize test data and expected results
        self.mock_data = '{"key1": "SGVsbG8gV29ybGQ=", "key2": "UHl0aG9uIENvZGUgUmVmaW5lcg=="}'
        self.expected_output = {'key1': 'Hello World', 'key2': 'Python Code Refiner'}
    def test_decode_base64(self):
        # Test decoding base64 encoded strings from a mock JSON file
        with patch('builtins.open', mock_open(read_data=self.mock_data)):
            result = task_func('dummy_file.json')
            self.assertEqual(result, self.expected_output)
    def test_empty_json(self):
        # Test handling of an empty JSON file
        with patch('builtins.open', mock_open(read_data='{}')):
            result = task_func('dummy_file.json')
            self.assertEqual(result, {})
    def test_non_json_content(self):
        # Test error handling for non-JSON content
        with patch('builtins.open', mock_open(read_data='Not a JSON')):
            with self.assertRaises(json.JSONDecodeError):
                task_func('dummy_file.json')
    def test_file_not_found(self):
        # Test error handling for a non-existent file
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_file.json')
    def test_invalid_base64(self):
        # Test error handling for invalid base64 encoding
        with patch('builtins.open', mock_open(read_data='{"key1": "Invalid base64"}')):
            with self.assertRaises(ValueError):
                task_func('dummy_file.json')
    def test_unicode_normalization(self):
        # Properly encode a Unicode string 'è' to base64
        unicode_string = 'è'
        encoded_unicode_string = base64.b64encode(unicode_string.encode('utf-8')).decode('ascii')
        mock_data_with_unicode = f'{{"key1": "{encoded_unicode_string}"}}'  # Encoded mock data
        expected_normalized_output = {'key1': 'è'}  # Expected result after normalization
        with patch('builtins.open', mock_open(read_data=mock_data_with_unicode)):
            result = task_func('dummy_file_unicode.json')
            self.assertEqual(result, expected_normalized_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)