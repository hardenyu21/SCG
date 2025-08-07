import ipaddress
import requests

def task_func(ip_range, timeout):
    try:
        # Validate and create a list of IP addresses from the CIDR range
        network = ipaddress.ip_network(ip_range, strict=False)
    except ValueError as e:
        raise ValueError("Invalid IP range provided.") from e

    active_ips = []

    for ip in network:
        try:
            # Send an HTTP GET request to the IP address
            response = requests.get(f"http://{ip}", timeout=timeout)
            # Check if the response status code is 200
            if response.status_code == 200:
                active_ips.append(str(ip))
        except requests.RequestException:
            # Ignore any request exceptions and continue to the next IP
            continue

    return active_ips
import unittest
from unittest.mock import patch, MagicMock
import requests  # Ensure requests is imported for exception handling
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_return_type(self, mock_get):
        """Test that the function returns a list."""
        mock_get.side_effect = requests.exceptions.ConnectionError
        # Adjusted to include required 'timeout' parameter
        result = task_func('192.168.0.0/30', 5)  
        self.assertIsInstance(result, list)
    @patch('requests.get')
    def test_handle_exceptions(self, mock_get):
        """Test that the function handles exceptions properly by not including IPs with failed requests."""
        mock_get.side_effect = [requests.exceptions.ConnectionError] * 4  # Assuming a /30 subnet, resulting in 4 attempts.
        result = task_func('192.168.0.0/30', 5)
        # The expected result is adjusted since the function no longer returns False for failed requests but instead skips them.
        expected_result = []  # Expecting an empty list due to ConnectionError.
        self.assertEqual(result, expected_result, "task_func should skip IPs that failed to connect.")
    @patch('requests.get')
    def test_active_server(self, mock_get):
        """
        Test that the function correctly identifies and includes active servers in the IP range.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        ip_range = '192.168.1.0/30'  
        result = task_func(ip_range, 5)
        expected_result = ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3']
        self.assertEqual(result, expected_result, "The function should identify and include all active servers in the range.")
    @patch('requests.get')
    def test_non_active_server(self, mock_get):
        """Test that non-active IP addresses are not included."""
        mock_get.return_value.status_code = 404
        result = task_func('192.168.0.0/30', 5)
        self.assertEqual(result, [], "Non-active IPs should not be included in the result.")
    @patch('requests.get')
    def test_full_range_iteration(self, mock_get):
        """
        Test that the function iterates over and makes a request to each IP in a complete /30 subnet.
        """
        mock_response = MagicMock(status_code=200)
        mock_get.return_value = mock_response
        ip_range = '192.168.1.0/30'
        result = task_func(ip_range, 5)
        expected_result_count = 4  # /30 network typically includes 4 IPs, but 2 are usable hosts
        self.assertEqual(len(result), expected_result_count)
        self.assertEqual(mock_get.call_count, expected_result_count, "Should make HTTP GET requests only to usable IPs.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)