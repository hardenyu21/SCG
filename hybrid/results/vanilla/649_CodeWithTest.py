import numpy as np
import pandas as pd
from dateutil.parser import parse

def task_func(dates_str_list):
    # Define the weekday names in order
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Initialize a list to store the weekday names
    weekday_counts = [0] * 7
    
    # Iterate over each date string in the list
    for date_str in dates_str_list:
        # Parse the date string to a datetime object
        date = parse(date_str)
        # Get the weekday as an integer (0=Monday, 6=Sunday)
        weekday_index = date.weekday()
        # Increment the count for the corresponding weekday
        weekday_counts[weekday_index] += 1
    
    # Create a pandas Series with the weekday distribution
    weekday_series = pd.Series(weekday_counts, index=weekdays)
    
    return weekday_series

# Example usage:
# dates = ["2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06", "2023-10-07", "2023-10-08"]
# print(task_func(dates))
import unittest
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1: Testing with a sample date list
        input_dates = ['2022-10-22', '2022-10-23', '2022-10-24', '2022-10-25']
        expected_output = pd.Series([1, 1, 0, 0, 0, 1, 1], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_2(self):
        # Input 2: Testing with a list where all dates fall on a single weekday
        input_dates = ['2022-10-24', '2022-10-31', '2022-11-07']
        expected_output = pd.Series([3, 0, 0, 0, 0, 0, 0], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_3(self):
        # Input 3: Testing with an empty list
        input_dates = []
        expected_output = pd.Series([0, 0, 0, 0, 0, 0, 0], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_4(self):
        # Input 4: Testing with a mixed list of dates
        input_dates = ['2022-01-01', '2022-02-14', '2022-03-17', '2022-12-31']
        expected_output = pd.Series([1, 0, 0, 1, 0, 2, 0], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_5(self):
        # Input 5: Testing with dates spanning multiple weeks
        input_dates = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07']
        expected_output = pd.Series([1, 1, 1, 1, 1, 1, 1], index=DAYS_OF_WEEK)
        result = task_func(input_dates)
        pd.testing.assert_series_equal(result, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)