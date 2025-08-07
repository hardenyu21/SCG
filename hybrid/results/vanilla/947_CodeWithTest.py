import numpy as np
import random
from datetime import datetime, timedelta

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Calculate the total number of days between start_date and end_date
    delta = end_date - start_date
    total_days = delta.days + 1
    
    # Ensure the number of unique dates required does not exceed the available days
    if rows * columns > total_days:
        raise ValueError("The number of unique dates requested exceeds the available days between start_date and end_date.")
    
    # Generate a list of unique dates
    unique_dates = [start_date + timedelta(days=i) for i in range(total_days)]
    random.shuffle(unique_dates)
    
    # Select the required number of unique dates
    selected_dates = unique_dates[:rows * columns]
    
    # Reshape the list of dates into a numpy ndarray
    date_matrix = np.array(selected_dates).reshape(rows, columns)
    
    return date_matrix

# Example usage:
# date_matrix = task_func(3, 2, datetime(2021, 1, 1), datetime(2021, 12, 31), seed=0)
# print(date_matrix)
# Unit testing
import unittest
import numpy.testing as npt
class TestCases(unittest.TestCase):
        
    def test_case_1(self):
        # Using default parameters
        matrix = task_func(seed=0)
        self.assertEqual(matrix.shape, (3, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) > 0))  # Dates should be unique
    def test_case_2(self):
        # Using custom rows and columns, and a small date range
        matrix = task_func(2, 2, datetime(2021, 1, 1), datetime(2021, 1, 10), seed=42)
        self.assertEqual(matrix.shape, (2, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
    def test_case_3(self):
        # Using custom rows and columns, and a large date range
        matrix = task_func(4, 4, datetime(2000, 1, 1), datetime(2021, 12, 31), seed=55)
        self.assertEqual(matrix.shape, (4, 4))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
    def test_case_4(self):
        # Using a date range of one day
        matrix = task_func(1, 1, datetime(2021, 1, 1), datetime(2021, 1, 1), seed=0)
        expected_date = np.array(['2021-01-01'], dtype='datetime64[us]').reshape(1, 1)
        npt.assert_array_equal(matrix, expected_date)  # Only one date in the range
    def test_case_5(self):
        # Using custom rows and columns, and a date range with only two days
        matrix = task_func(1, 2, datetime(2021, 1, 1), datetime(2021, 1, 2), seed=41)
        self.assertEqual(matrix.shape, (1, 2))
        self.assertTrue(np.all(np.diff(matrix.ravel()).astype(int) >= 0))  # Dates should be unique
        expected_dates = np.array(['2021-01-01', '2021-01-02'], dtype='datetime64[us]').reshape(1, 2)
        for date in expected_dates.ravel():
            self.assertIn(date, matrix.ravel())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)