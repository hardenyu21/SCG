import re
import requests
import csv
import os

# Constants
API_URL = 'https://api.example.com/data'

def task_func(pattern):
    # Make a GET request to the API
    response = requests.get(API_URL)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from API: {response.status_code}")
    
    # Parse the JSON response
    try:
        data = response.json()
    except json.JSONDecodeError:
        raise Exception("Failed to decode JSON response")
    
    # Extract the data from the JSON response
    if 'data' not in data:
        raise Exception("No 'data' key found in JSON response")
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Find all matches in the data
    matched_data = []
    for item in data['data']:
        if isinstance(item, str) and regex.search(item):
            matched_data.append([item])
    
    # Define the CSV file path
    csv_file_path = os.path.abspath("matched_data.csv")
    
    # Write the matched data to a CSV file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(matched_data)
    
    # Return the absolute path to the CSV file
    return csv_file_path
import unittest
from unittest.mock import patch, Mock
import os
def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data
            self.text = json.dumps(json_data)
        
        def json(self):
            return self.json_data
    if args[0] == 'https://api.example.com/data':
        return MockResponse(MOCK_API_RESPONSES.pop(0))
    return MockResponse(None)
MOCK_API_RESPONSES = [
    {"data": ["john.doe@example.com", "jane.smith@domain.org"]},
    {"data": ["123-45-6789", "987-65-4321"]},
    {"data": ["apple", "banana", "cherry"]},
    {"data": []},
    {"data": ["test1@example.com", "test2@domain.org", "123-45-6789", "apple"]}
]
class TestCases(unittest.TestCase):
    def setUp(self):
        if os.path.exists("matched_data.csv"):
            os.remove("matched_data.csv")
    def tearDown(self):
        if os.path.exists("matched_data.csv"):
            os.remove("matched_data.csv")
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, mock_get):
        result = task_func(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertIn("john.doe@example.com", content)
            self.assertIn("jane.smith@domain.org", content)
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, mock_get):
        result = task_func('\d{3}-\d{2}-\d{4}')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertIn("123-45-6789", content)
            self.assertIn("987-65-4321", content)
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, mock_get):
        result = task_func(r'apple')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertIn("apple", content)
            self.assertNotIn("banana", content)
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, mock_get):
        result = task_func(r'no_match')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertEqual(content, "")
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_5(self, mock_get):
        result = task_func(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        self.assertTrue(os.path.exists(result))
        with open("matched_data.csv", "r") as file:
            content = file.read()
            self.assertNotIn("john.doe@example.com", content)
            self.assertNotIn("jane.smith@domain.org", content)
            self.assertIn("test1@example.com", content)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)