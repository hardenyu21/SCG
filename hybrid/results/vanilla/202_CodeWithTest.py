import re
import json
from collections import Counter

def task_func(json_str, top_n=10):
    # Define a URL pattern
    url_pattern = r'https?://[^\s"]+'
    
    # Load the JSON string into a Python dictionary
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return {}
    
    # Convert the dictionary to a string to search for URLs
    data_str = json.dumps(data)
    
    # Find all URLs in the string using the regex pattern
    urls = re.findall(url_pattern, data_str)
    
    # Count the occurrences of each URL
    url_counts = Counter(urls)
    
    # Return the top_n URLs with their counts
    return dict(url_counts.most_common(top_n))

# Example usage:
# json_str = '{"links": ["http://example.com", "https://example.com", "http://example.com/page", "https://example.com"]}'
# print(task_func(json_str))
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        json_str = '{"name": "John", "website": "qwerthttps://www.example.com"}'
        result = task_func(json_str)
        self.assertEqual(result, {})
    def test_case_2(self):
        json_str = '{"name": "John", "social": {"twitter": "https://twitter.com/john", "linkedin": "https://linkedin.com/in/john"}, "website": "https://linkedin.com/in/john"}'
        result = task_func(json_str)
        self.assertEqual(result, {'https://twitter.com/john': 1, 'https://linkedin.com/in/john': 2})
        result = task_func(json_str, 1)
        self.assertEqual(result, {'https://linkedin.com/in/john': 2})
    def test_case_3(self):
        json_str = 'This is an adversarial input 0061'
        with self.assertRaises(json.decoder.JSONDecodeError):
            result = task_func(json_str)
    def test_case_4(self):
        json_str = '{"name": "John", "age": 30}'
        result = task_func(json_str)
        self.assertEqual(result, {})
    def test_case_5(self):
        json_str = '{"name": "John", "website": "example.com", "blog": "www.johnblog.com"}'
        result = task_func(json_str)
        self.assertEqual(result, {'www.johnblog.com': 1})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)