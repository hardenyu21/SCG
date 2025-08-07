import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    try:
        # Fetch the content of the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        webpage_content = response.text

        # Parse the webpage content
        soup = BeautifulSoup(webpage_content, 'html.parser')

        # Find all <script> tags
        script_tags = soup.find_all('script')

        # List to store successfully evaluated dictionaries
        evaluated_dicts = []

        # Iterate over each script tag
        for script in script_tags:
            script_content = script.string
            if script_content:
                # Attempt to evaluate the script content as a Python dictionary
                try:
                    # Use ast.literal_eval to safely evaluate the string
                    evaluated_content = ast.literal_eval(script_content)
                    # Check if the evaluated content is a dictionary
                    if isinstance(evaluated_content, dict):
                        evaluated_dicts.append(evaluated_content)
                except (ValueError, SyntaxError):
                    # If evaluation fails, continue to the next script tag
                    continue

        return evaluated_dicts

    except requests.RequestException:
        # Return an empty list if any error occurs during the request
        return []

# Example usage:
# result = task_func('https://example.com')
# print(result)
import unittest
from unittest.mock import patch, Mock
def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code
        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.RequestException("Mocked error")
    if args[0] == 'https://test1.com':
        return MockResponse('<script>{"key": "value"}</script>', 200)
    elif args[0] == 'https://test2.com':
        return MockResponse('<script>{"key1": "value1"}</script><script>{"key2": "value2"}</script>', 200)
    elif args[0] == 'https://test3.com':
        return MockResponse('<div>No script tags here</div>', 200)
    elif args[0] == 'https://test4.com':
        return MockResponse('<script>Not a dictionary</script>', 200)
    elif args[0] == 'https://error.com':
        return MockResponse('Error', 404)
    return MockResponse('', 404)
class TestCases(unittest.TestCase):
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, mock_get):
        # Test with a single dictionary in the script tag
        result = task_func('https://test1.com')
        self.assertEqual(result, [{"key": "value"}])
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self, mock_get):
        # Test with multiple dictionaries in separate script tags
        result = task_func('https://test2.com')
        self.assertEqual(result, [{"key1": "value1"}, {"key2": "value2"}])
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, mock_get):
        # Test with no script tags
        result = task_func('https://test3.com')
        self.assertEqual(result, [])
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, mock_get):
        # Test with a script tag that doesn't contain a dictionary
        result = task_func('https://test4.com')
        self.assertEqual(result, [])
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_5(self, mock_get):
        # Test with a URL that returns an error
        result = task_func('https://error.com')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)