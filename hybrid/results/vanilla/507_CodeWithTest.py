import pandas as pd
import numpy as np

def task_func(column, data):
    # Check if the data is empty
    if data.empty:
        return {
            'sum': 0,
            'mean': np.nan,
            'min': np.nan,
            'max': np.nan
        }
    
    # Check if the specified column exists in the data
    if column not in data.columns:
        raise ValueError("The specified column name is not valid.")
    
    # Calculate the required statistics
    column_data = data[column]
    result = {
        'sum': column_data.sum(),
        'mean': column_data.mean(),
        'min': column_data.min(),
        'max': column_data.max()
    }
    
    return result
import unittest
import numpy as np
from datetime import datetime
class TestCases(unittest.TestCase):
    def assertDictAlmostEqual(self, d1, d2, msg=None):
        # Helper function for testing
        for k, v in d1.items():
            if isinstance(v, float) and np.isnan(v):
                self.assertTrue(np.isnan(d2[k]), msg or f"{k} not almost equal")
            else:
                self.assertAlmostEqual(v, d2[k], msg=msg or f"{k} not equal")
    def test_case_1(self):
        # Test with valid data for a specific column
        data = [
            [datetime(2022, 1, 1), 100, 105, 95, 102, 10000],
            [datetime(2022, 1, 2), 102, 108, 100, 105, 15000],
            [datetime(2022, 1, 3), 105, 110, 103, 108, 20000],
        ]
        result = task_func("Open", data)
        expected_result = {
            "sum": 307,
            "mean": 102.33333333333333,
            "min": 100,
            "max": 105,
        }
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_2(self):
        # Test with empty data list
        data = []
        result = task_func("Open", data)
        expected_result = {
            "sum": 0,
            "mean": float("nan"),
            "min": float("nan"),
            "max": float("nan"),
        }
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_3(self):
        # Test with an invalid column name
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]]
        with self.assertRaises(ValueError):
            task_func("InvalidColumn", data)
    def test_case_4(self):
        # Test with NaN values in the target column
        data = [
            [datetime(2022, 1, 1), np.nan, 105, 95, 102, 10000],
            [datetime(2022, 1, 2), 102, np.nan, 100, 105, 15000],
            [datetime(2022, 1, 3), 105, np.nan, 103, 108, 20000],
        ]
        result = task_func("Open", data)
        expected_result = {"sum": 207, "mean": 103.5, "min": 102, "max": 105}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_5(self):
        # Test with all values in the target column being the same
        data = [[datetime(2022, 1, 1), 100, 100, 100, 100, 10000]] * 3
        result = task_func("Open", data)
        expected_result = {"sum": 300, "mean": 100, "min": 100, "max": 100}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_6(self):
        # Test for handling mixed data types within a single column
        data = [
            [datetime(2022, 1, 1), 100, 105, 95, 102, 10000],
            [datetime(2022, 1, 2), "102", 108, 100, 105, 15000],
        ]
        with self.assertRaises(TypeError):
            task_func("Open", data)
    def test_case_7(self):
        # Test with extremely large values in the target column
        data = [[datetime(2022, 1, 1), 1e18, 1.05e18, 0.95e18, 1.02e18, 10000]]
        result = task_func("Open", data)
        expected_result = {"sum": 1e18, "mean": 1e18, "min": 1e18, "max": 1e18}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_8(self):
        # Test with a single row of data
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]]
        result = task_func("Open", data)
        expected_result = {"sum": 100, "mean": 100, "min": 100, "max": 100}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_9(self):
        # Test with a very large dataset to check performance/scalability
        large_data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]] * 10000
        result = task_func("Open", large_data)
        expected_result = {"sum": 1000000, "mean": 100, "min": 100, "max": 100}
        self.assertDictAlmostEqual(result, expected_result)
    def test_case_10(self):
        # Test for column case sensitivity
        data = [
            [datetime(2022, 1, 1), 100, 105, 95, 102, 10000],
        ]
        with self.assertRaises(ValueError):
            task_func("open", data)
    def test_case_11(self):
        # Test with incorrect data
        data = "Incorrect data type"
        with self.assertRaises(ValueError):
            task_func("Open", data)
    def test_case_12(self):
        # Test for data list containing lists of varying lengths
        data = [
            [datetime(2022, 1, 1), 100, 105, 95, 102, 10000],
            [datetime(2022, 1, 2), 102, 108, 100],
        ]
        with self.assertRaises(ValueError):
            task_func("Open", data)
    def test_case_13(self):
        # Test for data list containing elements other than lists (mixed types)
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000], "Not a list"]
        with self.assertRaises(ValueError):
            task_func("Open", data)
    def test_case_14(self):
        # Test for a correctly structured and typed data list but with an empty inner list
        data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000], []]
        with self.assertRaises(ValueError):
            task_func("Open", data)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)