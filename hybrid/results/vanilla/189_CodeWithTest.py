import re
import json
import requests

def task_func(data_url: str) -> list:
    try:
        response = requests.get(data_url)
        response.raise_for_status()  # Ensure we handle HTTP errors
        data = response.text

        # Use regular expression to find names not enclosed in square brackets
        # This regex assumes names are alphanumeric and may include spaces
        names = re.findall(r'(?<!\[)"([A-Za-z\s]+)"(?!\])', data)

        return names

    except Exception:
        return "Invalid url input"
import unittest
from unittest.mock import patch
import json
import requests
class TestCases(unittest.TestCase):
    def mock_requests_get(url):
        # Sample mock response data with names
        if url == "https://api.example.com/data":
            response = requests.Response()
            response._content = json.dumps({"names": ["John", "Doe", "Alice"]}).encode('utf-8')
            return response
        elif url == "https://api.example.com/other_data":
            response = requests.Response()
            response._content = json.dumps({"names": ["Bob", "[Adam]", "Eve"]}).encode('utf-8')
            return response
        elif url == "https://api.example.com/data_1":
            response = requests.Response()
            response._content = json.dumps({"names": ["Billy"]}).encode('utf-8')
            return response
        else:
            return ""
        
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, mock_get):
        context = "https://api.example.com/data"
        result = task_func(context)
        self.assertListEqual(result, ["John", "Doe", "Alice"])
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, mock_get):
        context = "https://api.example.com/other_data"
        result = task_func(context)
        self.assertListEqual(result, ['Bob', 'Eve'])
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, mock_get):
        context = ""
        result = task_func(context)
        self.assertEqual(result, "Invalid url input")
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, mock_get):
        context = "https://api.example.com/error_data"
        result = task_func(context)
        self.assertEqual(result, "Invalid url input")
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_5(self, mock_get):
        context = "https://api.example.com/data_1"
        result = task_func(context)
        self.assertListEqual(result, ['Billy'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)