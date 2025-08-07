from dateutil.parser import parse
from datetime import timedelta

def task_func(date_str):
    # Parse the input date string into a datetime object
    date = parse(date_str)
    
    # Initialize a variable to hold the next business day
    next_business_day = date
    
    # Loop until we find the next business day (Monday to Friday)
    while True:
        # Move to the next day
        next_business_day += timedelta(days=1)
        
        # Check if the next day is a weekday (Monday=0, Sunday=6)
        if next_business_day.weekday() < 5:
            break
    
    return next_business_day
import unittest
from datetime import datetime
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        result = task_func('2022-10-22')
        self.assertEqual(result, datetime(2022, 10, 24, 0, 0))
    
    def test_case_2(self):
        result = task_func('2022-10-28')
        self.assertEqual(result, datetime(2022, 10, 31, 0, 0))
    
    def test_case_3(self):
        result = task_func('2022-10-30')
        self.assertEqual(result, datetime(2022, 10, 31, 0, 0))
    
    def test_case_4(self):
        result = task_func('2022-10-31')
        self.assertEqual(result, datetime(2022, 11, 1, 0, 0))
    
    def test_case_5(self):
        result = task_func('2022-11-02')
        self.assertEqual(result, datetime(2022, 11, 3, 0, 0))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)