import json
import csv
import requests
from io import StringIO

# Constants
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'

def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    # Download the CSV file from the specified URL
    response = requests.get(csv_url)
    response.raise_for_status()  # Raise an error for bad responses

    # Read the CSV data from the response
    csv_data = StringIO(response.text)
    csv_reader = csv.DictReader(csv_data)

    # Convert the CSV data to a list of dictionaries
    data_list = [row for row in csv_reader]

    # Convert the list of dictionaries to JSON format
    json_data = json.dumps(data_list, indent=4)

    # Save the JSON data to the specified file path
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

    # Return the path to the saved JSON file
    return json_file_path
import unittest
from unittest.mock import patch, Mock
import json
import csv
import requests
from io import StringIO
# Mocking the CSV data
mock_csv_data = """header1,header2,header3
value1a,value2a,value3a
value1b,value2b,value3b
"""
# Creating the mocked response object for the requests.get call
mock_response = Mock()
mock_response.text = mock_csv_data
# Blackbox test cases
class TestCases(unittest.TestCase):
    
    @patch("requests.get", return_value=mock_response)
    def test_case_1(self, mock_get):
        # Testing with default parameters
        output_file = task_func()
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['header1'], 'value1a')
        
    @patch("requests.get", return_value=mock_response)
    def test_case_2(self, mock_get):
        # Testing with custom parameters
        output_file = task_func("https://example.com/mock.csv", "mock_output.json")
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(data[1]['header2'], 'value2b')
        
    @patch("requests.get", return_value=mock_response)
    def test_case_3(self, mock_get):
        # Testing JSON structure
        output_file = task_func()
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertIn('header3', data[0])
        
    @patch("requests.get", return_value=mock_response)
    def test_case_4(self, mock_get):
        # Testing CSV with only headers (no data)
        mock_get.return_value.text = "header1,header2,header3\n"
        output_file = task_func()
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(len(data), 0)
        
    @patch("requests.get", return_value=mock_response)
    def test_case_5(self, mock_get):
        # Testing CSV with multiple data rows
        mock_get.return_value.text = mock_csv_data
        output_file = task_func()
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(len(data), 2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)