import pytz
import numpy as np
from dateutil.parser import parse
import math

MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    # Parse the date string and convert it to the target timezone
    date = parse(date_str)
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    date = from_timezone.localize(date).astimezone(to_timezone)
    
    # Calculate the number of days since the first reference year
    reference_year = MOON_PHASES_YEARS[0]
    days_since_reference = (date - datetime.datetime(reference_year, 1, 1, tzinfo=to_timezone)).days
    
    # Calculate the moon phase
    # The moon phase cycle is approximately 29.53 days
    lunar_cycle_days = 29.53
    moon_phase = (days_since_reference % lunar_cycle_days) / lunar_cycle_days
    
    return moon_phase

# Example usage:
# print(task_func("2023-10-01T12:00:00", "UTC", "America/New_York"))
import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Given a date in the past, in UTC timezone, convert to America/New_York timezone
        result = task_func('1970-01-01 00:00:00', 'UTC', 'America/New_York')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
    
    def test_case_2(self):
        # Given a date in the future, in Asia/Kolkata timezone, convert to Europe/London timezone
        result = task_func('2050-12-31 23:59:59', 'Asia/Kolkata', 'Europe/London')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
    def test_case_3(self):
        # Given a date close to a reference year in MOON_PHASES_YEARS, in UTC timezone, convert to America/New_York timezone
        result = task_func('2016-06-15 12:00:00', 'UTC', 'America/New_York')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
    
    def test_case_4(self):
        # Given a date far from any reference year in MOON_PHASES_YEARS, in America/Los_Angeles timezone, convert to Asia/Tokyo timezone
        result = task_func('2110-03-10 08:30:00', 'America/Los_Angeles', 'Asia/Tokyo')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1
    
    def test_case_5(self):
        # Given a date with a different date format, in UTC timezone, convert to America/New_York timezone
        result = task_func('01 Jan 1990 01:01:01', 'UTC', 'America/New_York')
        self.assertTrue(-1 <= result <= 1)  # The returned value should be between 0 and 1


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)