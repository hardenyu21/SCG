import re
import socket

def task_func(ip_addresses: list) -> dict:
    # Regular expression to validate IPv4 addresses
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    
    def is_valid_ip(ip):
        if ip_pattern.match(ip):
            # Check if each octet is between 0 and 255
            return all(0 <= int(octet) <= 255 for octet in ip.split('.'))
        return False

    ip_to_hostname = {}
    
    for ip in ip_addresses:
        if is_valid_ip(ip):
            try:
                # Get the hostname for the IP address
                hostname = socket.gethostbyaddr(ip)[0]
                ip_to_hostname[ip] = hostname
            except (socket.herror, socket.gaierror):
                # If hostname cannot be determined, set value to None
                ip_to_hostname[ip] = None
        else:
            # If the IP is not valid, set value to None
            ip_to_hostname[ip] = None
    
    return ip_to_hostname
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func(['8.8.8.8', '8.8.4.4'])
        expected = {'8.8.8.8': 'dns.google', '8.8.4.4': 'dns.google'}
        self.assertDictEqual(result, expected)
    def test_case_2(self):
        result = task_func(['8.8.4.4'])
        expected = {'8.8.4.4': 'dns.google'}
        self.assertDictEqual(result, expected)
    def test_case_3(self):
        result = task_func(['256.256.256.256'])
        expected = {'256.256.256.256': None}
        self.assertDictEqual(result, expected)
    def test_case_4(self):
        result = task_func([])
        expected = {}
        self.assertDictEqual(result, expected)
    def test_case_5(self):
        result = task_func(['1.1.1.1', '2.2.2.2'])
        expected_keys = ['1.1.1.1', '2.2.2.2']
        self.assertListEqual(list(result.keys()), expected_keys)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)