import pytz
from dateutil import parser

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string into a datetime object
    naive_datetime = parser.parse(date_str)
    
    # Localize the naive datetime to the source timezone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Convert the localized datetime to the target timezone
    to_timezone = pytz.timezone(to_tz)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    
    # Format the converted datetime as a string in "yyyy-mm-dd hh:mm:ss" format
    formatted_datetime = converted_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_datetime
import unittest
class TestCases(unittest.TestCase):
    def test_utc_to_new_york(self):
        """Test conversion from UTC to America/New_York timezone."""
        result = task_func('2022-03-01 12:00:00', 'UTC', 'America/New_York')
        self.assertEqual(result, '2022-03-01 07:00:00')
    def test_utc_to_los_angeles_summer_time(self):
        """Test conversion from UTC to America/Los_Angeles with daylight saving."""
        result = task_func('2022-06-01 12:00:00', 'UTC', 'America/Los_Angeles')
        self.assertEqual(result, '2022-06-01 05:00:00')
    def test_invalid_date_format(self):
        """Test handling of invalid date format."""
        with self.assertRaises(ValueError):
            task_func('invalid-date', 'UTC', 'America/New_York')
    def test_same_timezone_conversion(self):
        """Test conversion where from_tz and to_tz are the same."""
        result = task_func('2022-03-01 12:00:00', 'UTC', 'UTC')
        self.assertEqual(result, '2022-03-01 12:00:00')
    def test_utc_to_london_summer_time(self):
        """Test conversion from UTC to Europe/London during summer (BST)."""
        result = task_func('2022-06-01 12:00:00', 'UTC', 'Europe/London')
        self.assertEqual(result, '2022-06-01 13:00:00')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)