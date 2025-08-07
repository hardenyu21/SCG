from datetime import datetime, timedelta
import pytz
import calendar

def task_func(days_in_past=7):
    if days_in_past < 0:
        raise ValueError("days_in_past must be a non-negative integer.")
    
    # Get the current date in UTC
    utc_now = datetime.now(pytz.utc)
    
    # Calculate the date 'days_in_past' days ago
    target_date = utc_now - timedelta(days=days_in_past)
    
    # Get the weekday as an integer (0=Monday, 6=Sunday)
    weekday_index = target_date.weekday()
    
    # Get the weekday name
    weekday_name = calendar.day_name[weekday_index]
    
    return weekday_name
import unittest
from datetime import datetime, timedelta
import pytz
import calendar
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Default input
        result = task_func()
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 7 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=7)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_2(self):
        # Input 2: Test with 3 days in the past
        result = task_func(3)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 3 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=3)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_3(self):
        # Input 3: Test with 0 days in the past (today)
        result = task_func(0)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for today
        expected_date = datetime.now(pytz.UTC)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_4(self):
        # Input 4: Test with 30 days in the past (approximately a month ago)
        result = task_func(30)
        self.assertIsInstance(result, str)
        self.assertIn(result, list(calendar.day_name))
        # Ensure the result matches the expected output for 30 days ago
        expected_date = datetime.now(pytz.UTC) - timedelta(days=30)
        expected_weekday = calendar.day_name[expected_date.weekday()]
        self.assertEqual(result, expected_weekday)
    def test_case_5(self):
        # Input 5: Test handling invalid days_in_the_past
        for invalid in [-1, "1"]:
            with self.assertRaises(Exception):
                task_func(invalid)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)