import requests
import os
import json
import time

# Redefining the function in the current context
HEADERS = {
    'accept': 'text/json',
    'Content-Type': 'application/json'
}

def task_func(url, directory, metadata):
    # Check if the directory exists
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    
    # Check if the URL is valid
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        raise TypeError("The URL is invalid.")
    
    status_codes = []
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            # Prepare the data to be sent
            files = {'file': open(file_path, 'rb')}
            data = {'metadata': json.dumps(metadata)}
            
            try:
                # Send the POST request
                response = requests.post(url, headers=HEADERS, files=files, data=data)
                
                # Append the status code to the list
                status_codes.append(response.status_code)
                
                # Pause for one second
                time.sleep(1)
            finally:
                # Ensure the file is closed
                files['file'].close()
    
    return status_codes
import unittest
from unittest.mock import patch, Mock
import os
TEST_URL = "https://www.example.com"
TEST_DIRECTORY = "./test_uploads_task_func"
TEST_DIRECTORY_EMPTY = "./test_uploads_task_func_empty"
TEST_METADATA = {'userId': 'abc'}
# Mocking the requests.post method
def mock_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code
        
    # Simulate successful upload (status code 200)
    return MockResponse(200)
# Mocking the requests.post method fail
def mock_requests_post_fail(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code
        
    # Simulate fail upload (status code 404)
    return MockResponse(400)
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a test directory with dummy files
        os.makedirs(TEST_DIRECTORY, exist_ok=True)
        for i in range(5):
            with open(os.path.join(TEST_DIRECTORY, f"test_file_{i}.txt"), "w") as f:
                f.write(f"This is test file {i}")
        os.makedirs(TEST_DIRECTORY_EMPTY, exist_ok=True)
    def tearDown(self):
        # Remove the test directory and its contents after testing
        if os.path.exists(TEST_DIRECTORY):
            for file in os.listdir(TEST_DIRECTORY):
                os.remove(os.path.join(TEST_DIRECTORY, file))
            os.rmdir(TEST_DIRECTORY)
        if os.path.exists(TEST_DIRECTORY_EMPTY):
            os.rmdir(TEST_DIRECTORY_EMPTY)
    @patch('requests.post', side_effect=mock_requests_post)
    def test_upload_success(self, mock_post):
        # Test successful upload with mock response
        status_codes = task_func(TEST_URL, TEST_DIRECTORY, TEST_METADATA)
        self.assertEqual(status_codes, [200, 200, 200, 200, 200])
    @patch('requests.post', side_effect=mock_requests_post)
    def test_directory_not_found(self, mock_post):
        # Test if directory does not exist
        with self.assertRaises(FileNotFoundError):
            task_func(TEST_URL, "non_existing_directory", TEST_METADATA)
    @patch('requests.post', side_effect=mock_requests_post)
    def test_empty_directory(self, mock_post):
        # Test if directory is empty
        status_codes = task_func(TEST_URL, TEST_DIRECTORY_EMPTY, TEST_METADATA)
        self.assertEqual(status_codes, [])
    def test_invalid_url(self):
        # Test with invalid URL
        with self.assertRaises(Exception):
            task_func("invalid_url", TEST_DIRECTORY, TEST_METADATA)
    @patch('requests.post', side_effect=mock_requests_post_fail)
    def test_urls(self, mock_post):
        status_codes = task_func(TEST_URL, TEST_DIRECTORY, TEST_METADATA)
        self.assertEqual(status_codes, [400, 400, 400, 400, 400])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)