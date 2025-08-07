import re
import urllib.parse
import requests

def task_func(myString, API_KEY):
    # Regular expression to extract URLs from the string
    url_pattern = re.compile(r'https?://[^\s]+')
    urls = url_pattern.findall(myString)
    
    # Dictionary to store domain to geolocation data mapping
    domain_geolocation = {}
    
    for url in urls:
        # Parse the URL to extract the domain
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        # Skip if domain is empty
        if not domain:
            continue
        
        # Construct the API request URL
        api_url = f"http://ip-api.com/json/{domain}?key={API_KEY}"
        
        try:
            # Make the API request
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse the JSON response
            geolocation_data = response.json()
            
            # Store the geolocation data in the dictionary
            domain_geolocation[domain] = geolocation_data
        
        except requests.RequestException as e:
            # If the request fails, store None for this domain
            domain_geolocation[domain] = None
    
    return domain_geolocation
import unittest
from unittest.mock import patch
import json
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = json.dumps(json_data)
    def json(self):
        return self.json_data
def mocked_requests_get(*args, **kwargs):
    if 'google.com' in args[0]:
        return MockResponse({
            'status': 'success',
            'country': 'United States',
            'countryCode': 'US',
            'region': 'CA',
            'regionName': 'California',
            'city': 'Mountain View',
            'zip': '94043',
            'lat': '37.4192',
            'lon': '-122.0574',
            'timezone': 'America/Los_Angeles',
            'isp': 'Google LLC',
            'org': 'Google LLC',
            'as': 'AS15169 Google LLC',
            'query': '172.217.12.142'
        }, 200)
    elif 'python.org' in args[0]:
        return MockResponse({
            'status': 'success',
            'country': 'United States',
            'countryCode': 'US',
            'region': 'OR',
            'regionName': 'Oregon',
            'city': 'Boardman',
            'zip': '97818',
            'lat': '45.8696',
            'lon': '-119.688',
            'timezone': 'America/Los_Angeles',
            'isp': 'Amazon.com, Inc.',
            'org': 'Amazon Data Services NoVa',
            'as': 'AS16509 Amazon.com, Inc.',
            'query': '151.101.193.223'
        }, 200)
    else:
        raise Exception("API failure")
class TestCases(unittest.TestCase):
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_single_valid_url(self, mock_get):
        result = task_func("http://www.google.com", "TEST_API_KEY")
        self.assertEqual(result['www.google.com']['city'], 'Mountain View')
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_multiple_valid_urls(self, mock_get):
        result = task_func("http://www.google.com, https://www.python.org", "TEST_API_KEY")
        self.assertIn('www.python.org', result)
        self.assertEqual(result['www.python.org']['regionName'], 'Oregon')
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_no_urls(self, mock_get):
        result = task_func("This is a test without URLs.", "TEST_API_KEY")
        self.assertEqual(result, {})
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_url_scheme(self, mock_get):
        result = task_func("This is not a link: abc://test.link", "TEST_API_KEY")
        self.assertEqual(result, {})
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_repeated_urls(self, mock_get):
        result = task_func("http://www.google.com, http://www.google.com", "TEST_API_KEY")
        self.assertEqual(len(result), 1)  # Should only query once
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_api_failure_handling(self, mock_get):
        with self.assertRaises(Exception):
            result = task_func("http://nonexistent.domain.com", "TEST_API_KEY")
            self.assertIsNone(result.get('nonexistent.domain.com'))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)