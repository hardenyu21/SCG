import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_str, separator=",", bins=20):
    # Check if the input string is empty
    if not data_str.strip():
        raise ValueError("Data string is empty.")
    
    # Split the string into a list of values
    try:
        values = data_str.split(separator)
        # Convert the list of strings to a list of integers
        int_values = [int(value.strip()) for value in values]
    except ValueError:
        raise ValueError("Failed to convert data to integers.")
    
    # Create a pandas Series from the list of integers
    series = pd.Series(int_values, dtype='int64')
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(series, bins=bins, grid=True, rwidth=0.9, color='#607c8e')
    
    # Return the series and the Axes object
    return series, ax

# Example usage:
# series, ax = task_func("1,2,3,4,5,6,7,8,9,10")
# plt.show()
import unittest
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.default_str = "1,2,3,4,5,5,5,4,3,2,1"
        self.default_expected = pd.Series([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1])
    def assertHistogramAttributes(self, series, ax):
        # Check that the y-axis gridlines are set to True
        self.assertTrue(ax.yaxis.grid)
        # Ensure the histogram bars have the correct color
        self.assertEqual(matplotlib.colors.to_hex(ax.patches[0].get_fc()), "#607c8e")
        # Validate the heights of the histogram bars
        for patch in ax.patches:
            if (
                round(patch.get_x()) in series.values
                or round(patch.get_x() + patch.get_width()) in series.values
            ):
                self.assertTrue(patch.get_height() >= 0)
    def test_case_1(self):
        # Test default case
        series, ax = task_func(self.default_str)
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, self.default_expected)
    def test_case_2(self):
        # Test function works on different bin sizes
        for bins in [5, 10, 15, 30, 100]:
            with self.subTest(bins=bins):
                series, ax = task_func(self.default_str, bins=bins)
                self.assertIsInstance(series, pd.Series)
                self.assertHistogramAttributes(series, ax)
                pd.testing.assert_series_equal(series, self.default_expected)
    def test_case_3(self):
        # Test custom separators
        data_str = "1|2|3|4|5"
        series, ax = task_func(data_str, separator="|")
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, pd.Series([1, 2, 3, 4, 5]))
    def test_case_4(self):
        # Test negative and zero
        data_str = "-5,-4,-3,-2,-1,0"
        series, ax = task_func(data_str)
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, pd.Series([-5, -4, -3, -2, -1, 0]))
    def test_case_5(self):
        # Test single item
        data_str = "1"
        series, ax = task_func(data_str)
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, pd.Series([1]))
    def test_case_6(self):
        # Test with float
        series, ax = task_func("1.0,2.0,3.0,4.0,5.0,5.0,5.0,4.0,3.0,2.0,1.0")
        self.assertIsInstance(series, pd.Series)
        self.assertHistogramAttributes(series, ax)
        pd.testing.assert_series_equal(series, self.default_expected)
    def test_case_7(self):
        # Test with empty string
        data_str = ""
        with self.assertRaises(ValueError):
            task_func(data_str)
    def test_case_8(self):
        # Test with invalid data (contains string)
        data_str = "a,b,c, 1"
        with self.assertRaises(ValueError):
            task_func(data_str)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)