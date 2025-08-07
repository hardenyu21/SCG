import pandas as pd
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt

def task_func(start_date, end_date, num_series, seed=None):
    # Validate input parameters
    if start_date > end_date:
        raise ValueError("start_date must be earlier than end_date.")
    if num_series < 1:
        raise ValueError("num_series must be at least 1.")
    
    # Set random seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Generate date range
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Generate random time series data
    data = {}
    for i in range(num_series):
        series_name = f'series_{i+1}'
        data[series_name] = [random.randint(0, 100) for _ in date_range]
    
    # Create DataFrame
    df = pd.DataFrame(data, index=date_range)
    
    # Plot the time series
    ax = df.plot(title="Random Time Series", figsize=(10, 6))
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    plt.legend(title="Series")
    plt.grid(True)
    plt.tight_layout()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# df, ax = task_func(datetime(2023, 1, 1), datetime(2023, 1, 10), 3, seed=42)
# plt.show()
import unittest
import pandas as pd
import matplotlib
import warnings
class TestCases(unittest.TestCase):
    def test_valid_input(self):
        """Tests correct DataFrame structure and plot type with valid inputs."""
        df, ax = task_func("2022-01-01", "2022-01-10", 2, seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[1], 2)
        self.assertEqual(len(df.index), 10)
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes)
        self.assertTrue((df <= 100).all().all() and (df >= 0).all().all())
    def test_seed_reproducibility(self):
        """Tests if providing a seed results in reproducible outputs."""
        df1, _ = task_func("2022-01-01", "2022-01-05", 1, seed=42)
        df2, _ = task_func("2022-01-01", "2022-01-05", 1, seed=42)
        pd.testing.assert_frame_equal(df1, df2)
        self.assertTrue((df1 <= 100).all().all() and (df1 >= 0).all().all())
    def test_negative_num_series(self):
        """Tests if function raises an error when num_series is less than 1."""
        with self.assertRaises(ValueError):
            task_func("2022-01-01", "2022-01-10", 0)
    def test_start_date_after_end_date(self):
        """Tests if function raises an error when start date is after end date."""
        with self.assertRaises(ValueError):
            task_func("2022-01-10", "2022-01-01", 1)
    def test_single_day_series(self):
        """Tests DataFrame structure and plot type when start and end dates are the same."""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            df, ax = task_func("2022-07-01", "2022-07-01", 1, seed=42)
        self.assertEqual(len(df.index), 1)
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes)
        self.assertTrue((df <= 100).all().all() and (df >= 0).all().all())
    def test_multiple_series_names(self):
        """Tests if the generated DataFrame contains correct series names."""
        df, _ = task_func("2022-01-01", "2022-01-05", 3, seed=42)
        expected_columns = ["series_1", "series_2", "series_3"]
        self.assertListEqual(list(df.columns), expected_columns)
        self.assertTrue((df <= 100).all().all() and (df >= 0).all().all())
    def test_plot_attributes(self):
        """Tests the attributes of the plot, including title, x-label, and y-label."""
        _, ax = task_func("2022-01-01", "2022-01-05", 2, seed=42)
        self.assertEqual(ax.get_title(), "Random Time Series")
        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel(), "Value")
        self.assertTrue(len(ax.lines) == 2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)