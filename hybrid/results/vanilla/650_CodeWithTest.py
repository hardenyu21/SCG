from datetime import datetime, timedelta
import pytz
from dateutil.parser import parse

def task_func(date_str, tz_str):
    # Parse the input date string into a datetime object
    date = parse(date_str)
    
    # Localize the datetime object to the specified timezone
    timezone = pytz.timezone(tz_str)
    localized_date = timezone.localize(date)
    
    # Calculate the next New Year's Day in the same timezone
    next_new_year = datetime(localized_date.year + 1, 1, 1, tzinfo=timezone)
    
    # Calculate the difference in seconds until the next New Year
    time_until_next_new_year = (next_new_year - localized_date).total_seconds()
    
    return int(time_until_next_new_year)

# Example usage:
# print(task_func("2023-12-31T23:00:00", "America/New_York"))
import unittest
class TestCases(unittest.TestCase):
    def test_time_until_new_year(self):
        # Test with a specific date and timezone
        self.assertIsInstance(task_func('2023-12-31 23:59:59', 'UTC'), int)
    def test_start_of_year(self):
        # Test exactly at the start of a year
        self.assertIsInstance(task_func('2023-01-01 00:00:00', 'UTC'), int)
    def test_leap_year(self):
        # Test a date in a leap year
        self.assertIsInstance(task_func('2024-02-29 00:00:00', 'UTC'), int)
    def test_different_timezone(self):
        # Test with a non-UTC timezone
        self.assertIsInstance(task_func('2023-12-31 23:59:59', 'America/New_York'), int)
    def test_midyear(self):
        # Test a date in the middle of the year
        self.assertIsInstance(task_func('2023-06-15 12:00:00', 'UTC'), int)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)