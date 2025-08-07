import re
import json

# Constants
IP_REGEX = r'^(\d{1,3}\.){3}\d{1,3}$'

def is_valid_ip(ip_address):
    # Check if the IP address matches the regex pattern
    if re.match(IP_REGEX, ip_address):
        # Further validate that each octet is between 0 and 255
        parts = ip_address.split('.')
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False

def task_func(json_response):
    try:
        # Parse the JSON response
        data = json.loads(json_response)
        # Extract the IP address from the JSON
        ip_address = data.get('ip', '')
        # Validate the IP address
        if is_valid_ip(ip_address):
            return ip_address
        else:
            return 'Invalid IP address received'
    except (json.JSONDecodeError, ValueError):
        return 'Invalid JSON response'

# Example usage:
# json_response = '{"ip": "192.168.1.1"}'
# print(task_func(json_response))
import unittest
import json
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ip_address = json.dumps({'ip': '192.168.1.1'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '192.168.1.1')
    def test_case_2(self):
        ip_address = json.dumps({'ip': '500.500.500.500'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '500.500.500.500')
    def test_case_3(self):
        ip_address = json.dumps({'ip': '192.168.0.3'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, '192.168.0.3')
    def test_case_4(self):
        ip_address = json.dumps({'ip': ''}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, 'Invalid IP address received')
    def test_case_5(self):
        ip_address = json.dumps({'ip': 'Non-JSON response'}).encode('utf-8')
        
        result = task_func(ip_address)
        self.assertEqual(result, 'Invalid IP address received')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)