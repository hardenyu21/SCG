import pandas as pd
import numpy as np

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def task_func(df, dct):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame.")
    
    # Replace values in the DataFrame using the dictionary mapping
    df_replaced = df.replace(dct)
    
    # Calculate the Pearson correlation coefficient matrix
    correlation_matrix = df_replaced.corr(method='pearson')
    
    return correlation_matrix

# Example usage:
# df = pd.DataFrame({
#     'column1': [1, 2, 3, 4, 5],
#     'column2': [5, 4, 3, 2, 1],
#     'column3': [2, 3, 4, 5, 6],
#     'column4': [6, 5, 4, 3, 2],
#     'column5': [3, 4, 5, 6, 7]
# })
# dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# print(task_func(df, dct))
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with simple numeric DataFrame
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
        result = task_func(df, dct)
        self.assertTrue(result.shape == (2, 2))
    def test_case_2(self):
        # Test with DataFrame containing NaN values
        df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        dct = {1: 10, 2: 20, 4: 40, 6: 60}
        result = task_func(df, dct)
        self.assertTrue(result.isna().sum().sum() > 0)
    def test_case_3(self):
        # Test with DataFrame containing negative values
        df = pd.DataFrame({'A': [-1, -2, -3], 'B': [-4, -5, -6]})
        dct = {-1: 1, -2: 2, -3: 3, -4: 4, -5: 5, -6: 6}
        result = task_func(df, dct)
        self.assertTrue(result.shape == (2, 2))
    def test_case_4(self):
        # Test with DataFrame containing mixed data types
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        dct = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
        result = task_func(df, dct)
        self.assertTrue(result.shape == (2, 2))
    def test_case_5(self):
        # Test with larger DataFrame
        df = pd.DataFrame({'A': range(10), 'B': range(10, 20), 'C': range(20, 30)})
        dct = {i: i + 1 for i in range(30)}
        result = task_func(df, dct)
        self.assertTrue(result.shape == (3, 3))
    def test_case_6(self):
        with self.assertRaises(ValueError):
            task_func("non_df", {})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)