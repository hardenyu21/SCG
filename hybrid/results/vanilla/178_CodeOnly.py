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