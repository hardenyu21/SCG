from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(unix_timestamp, target_timezone):
    # Convert the Unix timestamp to a datetime object in UTC
    utc_dt = datetime.utcfromtimestamp(unix_timestamp)
    
    # Localize the UTC datetime to UTC timezone
    utc_dt = pytz.utc.localize(utc_dt)
    
    # Convert the datetime to the target timezone
    target_tz = pytz.timezone(target_timezone)
    target_dt = utc_dt.astimezone(target_tz)
    
    # Format the datetime object to the specified string format
    formatted_date = target_dt.strftime(DATE_FORMAT)
    
    return formatted_date
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func(1347517370, 'America/New_York')
        self.assertEqual(result, "2012-09-13 02:22:50")
    def test_case_2(self):
        result = task_func(0, 'UTC')
        self.assertEqual(result, "1970-01-01 00:00:00")
    def test_case_3(self):
        result = task_func(1609459200, 'Asia/Tokyo')
        self.assertEqual(result, "2021-01-01 09:00:00")
    def test_case_4(self):
        result = task_func(0, 'Asia/Kolkata')
        self.assertEqual(result, "1970-01-01 05:30:00")
    def test_case_5(self):
        result = task_func(1672531199, 'Australia/Sydney')
        self.assertEqual(result, "2023-01-01 10:59:59")
    def test_case_6(self):
        result = task_func(1609459200, 'America/New_York')
        self.assertEqual(result, "2020-12-31 19:00:00")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)