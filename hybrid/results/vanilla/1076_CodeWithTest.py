from datetime import datetime
import pandas as pd

# For Python versions lower than 3.9, use 'pytz' instead of 'zoneinfo'
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo

TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_strings, target_tz):
    # Initialize lists to store original and converted times
    original_times = []
    converted_times = []
    
    # Iterate over each time string in the input list
    for time_str in time_strings:
        # Parse the UTC time string into a datetime object
        utc_time = datetime.strptime(time_str, TIME_FORMAT)
        
        # Convert the UTC time to the specified timezone
        target_timezone = ZoneInfo(target_tz)
        converted_time = utc_time.astimezone(target_timezone)
        
        # Append the original and converted times to their respective lists
        original_times.append(utc_time)
        converted_times.append(converted_time)
    
    # Create a DataFrame with the original and converted times
    df = pd.DataFrame({
        'Original Time': original_times,
        'Converted Time': converted_times
    })
    
    return df

# Example usage:
# time_strings = ["01/01/22 12:00:00.000000", "02/01/22 13:30:00.000000"]
# target_tz = "America/New_York"
# df = task_func(time_strings, target_tz)
# print(df)
import unittest
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo
# Test cases
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_conversion_from_utc(self):
        """Test conversion from UTC to Eastern Standard Time."""
        time_strings = ["01/01/21 00:00:00.000", "01/01/21 12:00:00.000"]
        df = task_func(time_strings, "America/New_York")
        expected = ["31/12/20 19:00:00.000000", "01/01/21 07:00:00.000000"]
        self.assertEqual(list(df["Converted Time"]), expected)
    def test_conversion_from_non_utc(self):
        """Test conversion from Eastern Standard Time to India Standard Time."""
        time_strings = ["01/01/21 00:00:00.000", "01/01/21 12:00:00.000"]
        df = task_func(time_strings, "Asia/Kolkata")
        expected = ["01/01/21 05:30:00.000000", "01/01/21 17:30:00.000000"]
        self.assertEqual(list(df["Converted Time"]), expected)
    def test_empty_list(self):
        """Test empty list."""
        df = task_func([], "America/New_York")
        self.assertEqual(len(df), 0)
    def test_invalid_time_string(self):
        """Test invalid time string."""
        with self.assertRaises(ValueError):
            task_func(["invalid_time_string"], "America/New_York")
    def test_non_standard_time_format(self):
        """Test handling of non-standard time format."""
        time_strings = ["2021-01-01 00:00:00"]
        with self.assertRaises(ValueError):
            task_func(time_strings, "America/New_York")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)