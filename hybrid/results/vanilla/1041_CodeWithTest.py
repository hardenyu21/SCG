import re
import os

def task_func(request):
    # Define the base directory where static files are stored
    BASE_DIR = 'static_files'
    
    # Regular expression to extract the filename from the GET request
    GET_REQUEST_REGEX = r'^GET\s+/(.+?)\s+HTTP/1\.1$'
    
    # Match the request against the regex
    match = re.match(GET_REQUEST_REGEX, request)
    
    if not match:
        return "HTTP/1.1 400 Bad Request\r\n\r\nInvalid request format"
    
    # Extract the filename from the request
    filename = match.group(1)
    
    # Construct the full file path
    file_path = os.path.join(BASE_DIR, filename)
    
    # Check if the file exists and is a file
    if not os.path.isfile(file_path):
        return "HTTP/1.1 404 Not Found\r\n\r\nFile not found"
    
    # Read the file content
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
    except Exception as e:
        return f"HTTP/1.1 500 Internal Server Error\r\n\r\nError reading file: {str(e)}"
    
    # Prepare the HTTP response
    response = (
        f"HTTP/1.1 200 OK\r\n"
        f"Content-Length: {len(file_content)}\r\n"
        f"Content-Type: application/octet-stream\r\n"
        "\r\n"
    ).encode('utf-8') + file_content
    
    return response.decode('utf-8')
import unittest
import re
import os
from unittest.mock import mock_open, patch
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        """Set up the environment for testing by creating test files."""
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write("This is a test file.")
    def tearDown(self):
        """Clean up the environment by deleting the test files created."""
        os.remove("test.txt")
    def test_file_found(self):
        """Test the response when the requested file is found."""
        request = "GET /test.txt HTTP/1.1"
        expected_response = (
            "HTTP/1.1 200 OK\r\nContent-Length: 20\r\n\r\nThis is a test file."
        )
        self.assertEqual(task_func(request), expected_response)
    def test_file_not_found(self):
        """Test the response when the requested file is not found."""
        request = "GET /nonexistent.txt HTTP/1.1"
        expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
        self.assertEqual(task_func(request), expected_response)
    def test_bad_request(self):
        """Test the response for a badly formatted request."""
        request = "BAD REQUEST"
        expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
        self.assertEqual(task_func(request), expected_response)
    def test_empty_request(self):
        """Test the response for an empty request."""
        request = ""
        expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
        self.assertEqual(task_func(request), expected_response)
    def test_invalid_method_request(self):
        """Test the response for a request with an invalid HTTP method."""
        request = "POST /test.txt HTTP/1.1"
        expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
        self.assertEqual(task_func(request), expected_response)
    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_internal_server_error(self, mock_file):
        """Test the response when there's an internal server error (e.g., file read error)."""
        mock_file.side_effect = Exception("Mocked exception")
        request = "GET /test.txt HTTP/1.1"
        expected_response = (
            "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
        )
        self.assertEqual(task_func(request), expected_response)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)