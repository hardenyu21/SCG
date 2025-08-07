import pandas as pd
from random import uniform

def task_func(n_data_points=1000, min_value=0.0, max_value=10.0, column_name='Value'):
    # Generate random floating-point numbers
    data = [uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_data = [round(num, 3) for num in data]
    
    # Create a DataFrame with the specified column name
    df = pd.DataFrame(truncated_data, columns=[column_name])
    
    return df

# Example usage:
# df = task_func()
# print(df)
import unittest
import random
class TestCases(unittest.TestCase):
    def test_dataframe_type(self):
        """Test if the returned object is a pandas DataFrame."""
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, pd.DataFrame, "Returned object is not a pandas DataFrame")
    def test_dataframe_size(self):
        """Test if the DataFrame contains the correct number of data points."""
        random.seed(0)
        result = task_func()
        self.assertEqual(len(result), 1000, "DataFrame does not contain 1000 data points")
    def test_value_range(self):
        """Test if values are within the specified range."""
        random.seed(0)
        result = task_func(100)
        for value in result['Value']:
            self.assertGreaterEqual(value, 0.0, "Value is less than 0.0")
            self.assertLessEqual(value, 10.0, "Value is greater than 10.0")
    def test_decimal_precision(self):
        """Test if values have up to 3 decimal places."""
        random.seed(0)
        result = task_func(10, 5.0, 8.0)
        for value in result['Value']:
            self.assertLessEqual(len(str(value).split('.')[1]), 3, "Value does not have up to 3 decimal places")
    def test_dataframe_columns(self):
        """Test if the DataFrame has the correct column name."""
        random.seed(0)
        column_name = 'User'
        result = task_func(10, 5.0, 8.0, column_name)
        self.assertIn(column_name, result.columns, "DataFrame does not have a column named "+column_name)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)