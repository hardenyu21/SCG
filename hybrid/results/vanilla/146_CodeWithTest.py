import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    """
    Scans the specified IP address range and pings each IP to check if it is active.
    
    Args:
    ip_range (str): The IP address range in CIDR notation (e.g., '192.168.1.0/24').
    
    Returns:
    dict: A dictionary mapping IP addresses to their active status (True if active, False otherwise).
    
    Raises:
    subprocess.CalledProcessError: If a ping command fails due to a subprocess error.
    """
    ip_network = IPv4Network(ip_range)
    active_ips = {}

    for ip in ip_network:
        try:
            # Ping the IP address
            response = subprocess.run(['ping', '-c', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Check if the ping was successful
            if response.returncode == 0:
                active_ips[str(ip)] = True
            else:
                active_ips[str(ip)] = False
        except subprocess.CalledProcessError as e:
            raise subprocess.CalledProcessError(response.returncode, response.args, response.stdout, response.stderr) from e

    return active_ips
import unittest
from unittest.mock import patch
import subprocess
class TestCases(unittest.TestCase):
    @patch('subprocess.check_output')
    def test_return_type(self, mock_check_output):
        """
        Test that task_func returns a dictionary.
        """
        mock_check_output.return_value = b''  # Simulate successful ping response as empty byte string
        result = task_func('192.168.1.0/30')  # Using a smaller range for testing
        self.assertIsInstance(result, dict, "The function should return a dictionary.")
    @patch('subprocess.check_output')
    def test_successful_ping(self, mock_check_output):
        """
        Test that a successful ping sets the IP status to True.
        """
        mock_check_output.return_value = b''  # Simulate successful ping response
        result = task_func('192.168.1.0/30')
        self.assertTrue(all(result.values()), "All IPs should have True status for a successful ping.")
    @patch('subprocess.check_output', side_effect=subprocess.CalledProcessError(1, 'ping'))
    def test_failed_ping(self, mock_check_output):
        """
        Test that a failed ping sets the IP status to False.
        """
        result = task_func('192.168.1.0/30')
        self.assertTrue(all(not value for value in result.values()), "All IPs should have False status for a failed ping.")
    @patch('subprocess.check_output')
    def test_dict_key_value_types(self, mock_check_output):
        """
        Test that all keys and values in the dictionary returned by task_func are of the correct type.
        """
        mock_check_output.return_value = b''  # Simulate successful ping response
        result = task_func('192.168.1.0/30')  # Using a smaller range for testing
        for ip, status in result.items():
            self.assertIsInstance(ip, str, "All keys in the dictionary should be strings representing IP addresses.")
            self.assertIsInstance(status, bool, "All values in the dictionary should be boolean indicating the IP's active status.")
    @patch('subprocess.check_output')
    def test_ip_range_handling(self, mock_check_output):
        """
        Test that the function attempts to ping every IP in the specified range.
        """
        ip_range = '192.168.1.0/30'
        expected_call_count = len(list(IPv4Network(ip_range)))
        mock_check_output.return_value = b''  # Simulate successful ping response
        task_func(ip_range)
        self.assertEqual(mock_check_output.call_count, expected_call_count, f"Expected to attempt pinging {expected_call_count} IPs.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)