import unicodedata
import requests

URL = 'https://api.github.com/users/'

def task_func(username):
    try:
        response = requests.get(URL + username)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        user_data = response.json()
        
        # Normalize all string data to ASCII
        normalized_data = {}
        for key, value in user_data.items():
            if isinstance(value, str):
                normalized_data[key] = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
            else:
                normalized_data[key] = value
        
        return normalized_data
    
    except requests.exceptions.HTTPError as http_err:
        raise requests.exceptions.HTTPError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"An error occurred: {err}")

# Example usage:
# user_info = task_func('octocat')
# print(user_info)
import unittest
from unittest.mock import patch, Mock
import requests
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_return_type(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'name': 'Test User'}
        result = task_func('user')
        self.assertIsInstance(result, dict)
    @patch('requests.get')
    def test_normalized_string(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'name': 'Tést Üser'}
        result = task_func('user')
        self.assertEqual(result['name'], 'Test User')
    @patch('requests.get')
    def test_non_string_values(self, mock_get):
        mock_get.return_value.json.return_value = {'login': 'user', 'id': 12345}
        result = task_func('user')
        self.assertEqual(result['id'], 12345)
    @patch('requests.get')
    def test_empty_username(self, mock_get):
        mock_get.return_value.json.return_value = {}
        result = task_func('')
        self.assertEqual(result, {})
    @patch('requests.get')
    def test_error_response(self, mock_get):
        mock_get.return_value.raise_for_status = Mock(side_effect=requests.exceptions.HTTPError("404 Not Found"))
        with self.assertRaises(Exception) as context:
            task_func('nonexistentuser')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)