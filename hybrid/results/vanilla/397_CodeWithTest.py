import re
import urllib.request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(API_URL):
    try:
        # Make a request to the API
        with urllib.request.urlopen(API_URL) as response:
            # Read the response
            data = response.read().decode('utf-8')
            
            # Try to parse the response as JSON
            try:
                json_data = json.loads(data)
                # Check if the JSON contains a key that typically holds the IP address
                if 'ip' in json_data:
                    ip_address = json_data['ip']
                else:
                    # If not, use regex to find an IP address in the response
                    match = re.search(IP_REGEX, data)
                    if match:
                        ip_address = match.group(0)
                    else:
                        raise ValueError("IP address not found in the response.")
            except json.JSONDecodeError:
                # If JSON parsing fails, use regex to find an IP address in the response
                match = re.search(IP_REGEX, data)
                if match:
                    ip_address = match.group(0)
                else:
                    raise ValueError("IP address not found in the response.")
            
            # Validate the IP address format
            if not re.match(IP_REGEX, ip_address):
                raise ValueError("Invalid IP address format.")
            
            return ip_address
    except urllib.error.URLError as e:
        # Raise an exception if the API request fails
        raise Exception(f"API request failed: {e.reason}")
    except Exception as e:
        # Raise any other exceptions that may occur
        raise Exception(f"An error occurred: {str(e)}")

# Example usage:
# print(task_func("https://api.ipify.org?format=json"))
import unittest
from unittest.mock import patch, MagicMock
import json
class TestCases(unittest.TestCase):
    API_URL = 'https://api.ipify.org?format=json'
    @patch('urllib.request.urlopen')
    def test_valid_ip(self, mock_urlopen):
        # Mocking a valid IP response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({'ip': '192.168.1.1'}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        result = task_func(self.API_URL)
        self.assertEqual(result, '192.168.1.1')
    @patch('urllib.request.urlopen')
    def test_invalid_ip(self, mock_urlopen):
        # Mocking an invalid IP response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({'ip': '500.500.500.500'}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        result = task_func(self.API_URL)
        self.assertEqual(result, '500.500.500.500')
    @patch('urllib.request.urlopen')
    def test_api_failure(self, mock_urlopen):
        # Mocking an API failure
        mock_response = MagicMock()
        mock_urlopen.side_effect = Exception("API failure")
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        result = task_func(self.API_URL)
        self.assertTrue("API failure" in result)
    @patch('urllib.request.urlopen')
    def test_missing_ip_key(self, mock_urlopen):
        # Mocking response missing the 'ip' key
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None
        result = task_func(self.API_URL)
        self.assertEqual(result, "'ip'")
    @patch('urllib.request.urlopen')
    def test_non_json_response(self, mock_urlopen):
        # Mocking a non-JSON response from API
        mock_response = MagicMock()
        mock_response.read.return_value = "Non-JSON response".encode('utf-8')
        mock_urlopen.return_value = mock_response
        mock_response.__enter__.return_value = mock_response
        mock_response.__exit__.return_value = None


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)