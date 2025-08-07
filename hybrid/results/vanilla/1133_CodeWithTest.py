import json
import requests

def task_func(API_URL, endpoint, PREFIX):
    try:
        # Construct the full API endpoint URL
        full_url = f"{API_URL}/{endpoint}"
        
        # Fetch data from the API
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON data
        data = response.json()
        
        # Generate the filename
        filename = f"{PREFIX}{endpoint}.json"
        
        # Write the JSON data to a file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        
        # Return the filename
        return filename
    
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching data from API: {e}")
    except (IOError, OSError) as e:
        raise RuntimeError(f"Error writing to file: {e}")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Error decoding JSON data: {e}")
import unittest
from unittest.mock import patch, Mock
import os
import json
class TestCases(unittest.TestCase):    
    def tearDown(self):
        # Cleanup the directory after tests
        for filename in ("PREFIX_data.json", "PREFIX_empty.json", "PREFIX_temp.json"):
            if os.path.exists(filename):
                os.remove(filename)
    @patch('requests.get')
    def test_successful_data_fetch(self, mock_get):
        # Test successful API call and file creation with correct data
        mock_data = {'name': 'test', 'value': 123}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_data)
        api_url = 'https://fakeapi.com/'
        endpoint = 'data'
        prefix = 'PREFIX_'
        expected_filename = prefix + endpoint + '.json'
        result = task_func(api_url, endpoint, prefix)
        
        self.assertEqual(result, expected_filename)
        with open(result, 'r') as file:
            data = json.load(file)
        self.assertEqual(data, mock_data)
    @patch('requests.get')
    def test_empty_response_handling(self, mock_get):
        # Test function's handling of an empty response from the API
        mock_get.return_value = Mock(status_code=200, json=lambda: {})
        api_url = 'https://fakeapi.com/'
        endpoint = 'empty'
        prefix = 'PREFIX_'
        expected_filename = prefix + endpoint + '.json'
        with patch('os.path.join', return_value=expected_filename):
            result = task_func(api_url, endpoint, prefix)
        self.assertEqual(result, expected_filename)
    @patch('requests.get')
    def test_successful_data_fetch_different_filename(self, mock_get):
        # Test successful API call and file creation with correct data
        mock_data = {'name': 'test', 'value': 123}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_data)
        api_url = 'https://fakeapi.com/'
        endpoint = 'temp'
        prefix = 'PREFIX_'
        expected_filename = prefix + endpoint + '.json'
        with patch('os.path.join', return_value=expected_filename):
            result = task_func(api_url, endpoint, prefix)
        self.assertEqual(result, expected_filename)
    @patch('requests.get')
    def test_successful_data_fetch_and_content_check(self, mock_get):
        # Test successful API call and file creation with correct data and content check
        mock_data = {'name': 'test', 'value': 123}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_data)
        api_url = 'https://fakeapi.com/'
        endpoint = 'data'
        prefix = 'PREFIX_'
        expected_filename = prefix + endpoint + '.json'
        result = task_func(api_url, endpoint, prefix)
        
        self.assertEqual(result, expected_filename)
        with open(result, 'r') as file:
            content = json.load(file)
        self.assertEqual(content, mock_data)
        self.assertIn('name', content)
        self.assertIn('value', content)
        self.assertEqual(content['name'], 'test')
        self.assertEqual(content['value'], 123)
    @patch('requests.get')
    def test_empty_response_content(self, mock_get):
        # Test handling of an empty JSON response from the API and content check
        mock_get.return_value = Mock(status_code=200, json=lambda: {})
        api_url = 'https://fakeapi.com/'
        endpoint = 'empty'
        prefix = 'PREFIX_'
        expected_filename = prefix + endpoint + '.json'
        result = task_func(api_url, endpoint, prefix)
        
        self.assertEqual(result, expected_filename)
        with open(result, 'r') as file:
            content = json.load(file)
        self.assertEqual(content, {})  # Ensuring the file content is indeed empty as expected


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)