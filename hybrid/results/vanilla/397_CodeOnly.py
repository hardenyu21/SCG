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