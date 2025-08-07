import requests
import json
import base64

def task_func(data, url="http://your-api-url.com"):
    # Convert the dictionary to a JSON-formatted string
    json_string = json.dumps(data)
    
    # Encode the JSON string in base64 format
    base64_encoded = base64.b64encode(json_string.encode('utf-8')).decode('utf-8')
    
    # Prepare the payload for the POST request
    payload = {'payload': base64_encoded}
    
    # Send the POST request to the API endpoint
    response = requests.post(url, json=payload)
    
    # Return the response object
    return response
import unittest
from unittest.mock import patch, Mock
import requests
import json
# Mocking the requests.post method
def mock_post(*args, **kwargs):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "OK"
    return mock_response
class TestCases(unittest.TestCase):
    @patch('requests.post', side_effect=mock_post)
    def test_case_1(self, mock_post_method):
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        response = task_func(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")
    
    @patch('requests.post', side_effect=mock_post)
    def test_case_2(self, mock_post_method):
        data = {'task': 'Write code', 'status': 'completed'}
        response = task_func(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")
    @patch('requests.post', side_effect=mock_post)
    def test_case_3(self, mock_post_method):
        data = {}
        response = task_func(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")
    @patch('requests.post', side_effect=mock_post)
    def test_case_4(self, mock_post_method):
        data = {'fruit': 'apple', 'color': 'red', 'taste': 'sweet'}
        response = task_func(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")
    @patch('requests.post', side_effect=mock_post)
    def test_case_5(self, mock_post_method):
        data = {'country': 'USA', 'capital': 'Washington, D.C.'}
        response = task_func(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")
    @patch('requests.post', side_effect=mock_post)
    def test_case_6(self, mock_post_method):
        # Test to verify that the POST request is made with the correct parameters
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        json_data = json.dumps(data)
        encoded_data = base64.b64encode(json_data.encode('ascii')).decode('ascii')
        task_func(data, url="http://mock-api-url.com")
        try:
            mock_post_method.assert_called_once_with("http://mock-api-url.com", data={"payload": encoded_data})
        except:
            mock_post_method.assert_called_once_with("http://mock-api-url.com", json={"payload": encoded_data})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)