import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    # Load JSON data
    data = json.loads(json_str)
    
    # Helper function to remove None values and replace emails
    def process_value(value):
        if isinstance(value, dict):
            return {k: process_value(v) for k, v in value.items() if v is not None}
        elif isinstance(value, list):
            return [process_value(v) for v in value if v is not None]
        elif isinstance(value, str) and re.match(r"[^@]+@[^@]+\.[^@]+", value):
            return REPLACE_NONE
        else:
            return value
    
    # Process the data
    processed_data = process_value(data)
    
    # Flatten the data to count values
    def flatten(data):
        if isinstance(data, dict):
            for v in data.values():
                yield from flatten(v)
        elif isinstance(data, list):
            for item in data:
                yield from flatten(item)
        else:
            yield data
    
    # Count the frequency of each unique value
    value_counts = Counter(flatten(processed_data))
    
    # Return the result
    return {
        "data": processed_data,
        "value_counts": value_counts
    }
import unittest
import json
from collections import Counter
class TestCases(unittest.TestCase):
    def test_basic(self):
        json_str = '{"name": "John", "age": null, "email": "john@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
        self.assertEqual(result, expected)
    def test_multiple_none(self):
        json_str = '{"name": "John", "age": null, "city": null, "email": "john@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
        self.assertEqual(result, expected)
    def test_multiple_emails(self):
        json_str = '{"name": "John", "email1": "john1@example.com", "email2": "john2@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email1': 'None', 'email2': 'None'}, 'value_counts': Counter({'None': 2, 'John': 1})}
        self.assertEqual(result, expected)
    def test_no_emails(self):
        json_str = '{"name": "John", "age": 25, "city": "NY"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'age': 25, 'city': 'NY'}, 'value_counts': Counter({'John': 1, 25: 1, 'NY': 1})}
        self.assertEqual(result, expected)
    def test_different_values(self):
        json_str = '{"name": "John", "age": 25, "city": "NY", "friend": "John"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'age': 25, 'city': 'NY', 'friend': 'John'}, 'value_counts': Counter({'John': 2, 25: 1, 'NY': 1})}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)