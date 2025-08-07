import json
from datetime import datetime

def task_func(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    
    # Extract the 'utc_datetime' value
    utc_datetime_str = data.get('utc_datetime')
    
    # Convert the string to a datetime object
    utc_datetime = datetime.fromisoformat(utc_datetime_str)
    
    # Determine if the date is a weekend (Saturday or Sunday)
    # weekday() returns 5 for Saturday and 6 for Sunday
    is_weekend = utc_datetime.weekday() in (5, 6)
    
    return is_weekend
import unittest
from datetime import datetime
import json
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Create a datetime object for a weekday (Monday)
        utc_datetime = datetime(2024, 4, 15, 12, 0, 0)  # Monday, April 15, 2024
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = task_func(json_data)
        self.assertFalse(result)  # Monday is not a weekend)
    def test_saturday(self):
        # Create a datetime object for a Saturday
        utc_datetime = datetime(2024, 4, 13, 12, 0, 0)  # Saturday, April 13, 2024
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = task_func(json_data)
        self.assertTrue(result)  # Saturday is a weekend day
    def test_sunday(self):
        # Create a datetime object for a Sunday
        utc_datetime = datetime(2024, 4, 14, 12, 0, 0)  # Sunday, April 14, 2024
        json_data = json.dumps({'utc_datetime': utc_datetime.isoformat()})
        result = task_func(json_data)
        self.assertTrue(result)  # Sunday is a weekend day
    def test_empty_json(self):
        # Test with empty JSON input
        json_data = json.dumps({})
        with self.assertRaises(KeyError):
            task_func(json_data)
    def test_no_utc_datetime(self):
        # Test with JSON input missing 'utc_datetime' key
        json_data = json.dumps({'date': '2024-04-14T12:00:00'})
        with self.assertRaises(KeyError):
            task_func(json_data)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)