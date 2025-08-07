import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    naive_datetime = parse(date_str)
    
    # Localize the naive datetime to the source time zone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Convert the localized datetime to the destination time zone
    to_timezone = pytz.timezone(to_tz)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    
    # Get the current time in the destination time zone
    current_time = to_timezone.localize(parse('now'))
    
    # Calculate the time difference in seconds
    time_difference = (current_time - converted_datetime).total_seconds()
    
    return int(time_difference)
import unittest
from datetime import datetime, timedelta
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test conversion from UTC to America/Chicago with a date in the past
        result = task_func('2022-01-01 11:59:59', 'UTC', 'America/Chicago')
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
    def test_case_2(self):
        # Test conversion from America/New_York to Asia/Kolkata with a date in the past
        result = task_func('2022-01-01 11:59:59', 'America/New_York', 'Asia/Kolkata')
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
    def test_known_time_zone_offset_difference(self):
        """Test the function with time zones having a known, static offset."""
        known_date_utc = '2023-01-01 12:00:00'
        utc_zone = 'UTC'
        target_zone = 'Etc/GMT+2'
        try:
            result = task_func(known_date_utc, utc_zone, target_zone)
            self.assertTrue(isinstance(result, int), "Result should be an integer representing seconds.")
        except Exception as e:
            self.fail(f"task_func raised an exception with known static offset time zones: {e}")
    def test_case_4(self):
        # Test conversion with a future date from UTC to America/Chicago
        future_date = (datetime.utcnow() + timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S')
        result = task_func(future_date, 'UTC', 'America/Chicago')
        self.assertIsInstance(result, int)
        self.assertLess(result, 0)
    def test_case_5(self):
        # Test conversion from Asia/Kolkata to America/Los_Angeles with a date in the past
        result = task_func('2022-01-01 11:59:59', 'Asia/Kolkata', 'America/Los_Angeles')
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)