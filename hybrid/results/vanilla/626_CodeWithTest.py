from random import choice
import pytz
from dateutil.parser import parse

# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']

def task_func(date_str, from_tz):
    # Parse the input date string into a datetime object
    naive_datetime = parse(date_str)
    
    # Localize the naive datetime to the source timezone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Choose a random timezone from the list
    to_tz = choice(TIMEZONES)
    
    # Convert the localized datetime to the randomly chosen timezone
    to_timezone = pytz.timezone(to_tz)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    
    # Format the converted datetime as a string
    converted_datetime_str = converted_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    return (converted_datetime_str, to_tz)

# Example usage:
# result = task_func('2023-10-01 12:00:00', 'UTC')
# print(result)
import unittest
from datetime import datetime
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('2023-06-15 12:00:00', 'UTC')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
    
    def test_case_2(self):
        result = task_func('2022-01-01 00:00:00', 'America/New_York')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
        
    def test_case_3(self):
        result = task_func('2020-12-31 23:59:59', 'Asia/Shanghai')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
        
    def test_case_4(self):
        result = task_func('2019-07-04 04:04:04', 'Europe/London')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)
    
    def test_case_5(self):
        result = task_func('2018-02-28 14:28:58', 'Australia/Sydney')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        datetime_obj = datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(datetime_obj, datetime)
        self.assertIn(result[1], TIMEZONES)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)