import pytz
from dateutil.parser import parse

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_string, from_tz, to_tz):
    # Parse the input time string into a datetime object
    naive_datetime = parse(time_string)
    
    # Localize the naive datetime to the source timezone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Convert the localized datetime to the target timezone
    to_timezone = pytz.timezone(to_tz)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    
    # Format the converted datetime to the desired string format
    converted_time_string = converted_datetime.strftime(TIME_FORMAT)
    
    return converted_time_string

# Example usage:
# print(task_func("01/01/22 12:00:00.000", "America/New_York", "Europe/London"))
import unittest
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_utc_to_est(self):
        """
        Test conversion from UTC to Eastern Standard Time.
        """
        result = task_func("30/03/09 16:31:32.123", "UTC", "America/New_York")
        expected = "30/03/09 12:31:32.123000"  # Adjusted for daylight saving time if applicable
        self.assertEqual(result, expected)
    def test_est_to_utc(self):
        """
        Test conversion from Eastern Standard Time to UTC.
        """
        result = task_func("30/03/09 12:31:32.123", "America/New_York", "UTC")
        expected = "30/03/09 16:31:32.123000"  # Adjusted for daylight saving time if applicable
        self.assertEqual(result, expected)
    def test_utc_to_ist(self):
        """
        Test conversion from UTC to Indian Standard Time.
        """
        result = task_func("01/04/09 00:00:00.000", "UTC", "Asia/Kolkata")
        expected = "01/04/09 05:30:00.000000"  # IST is UTC+5:30
        self.assertEqual(result, expected)
    def test_ist_to_utc(self):
        """
        Test conversion from Indian Standard Time to UTC.
        """
        result = task_func("01/04/09 05:30:00.000", "Asia/Kolkata", "UTC")
        expected = "01/04/09 00:00:00.000000"  # IST is UTC+5:30
        self.assertEqual(result, expected)
    def test_utc_to_gmt(self):
        """
        Test conversion from UTC to GMT (should be the same).
        """
        result = task_func("15/04/09 10:30:00.000", "UTC", "GMT")
        expected = "15/04/09 10:30:00.000000"  # GMT and UTC are the same
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)