import numpy as np
import pandas as pd
from scipy.stats import linregress

def task_func(df, x_col, y_col):
    """
    Perform linear regression on two variables in a DataFrame and add a 'predicted' column.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    x_col (str): The name of the column to be used as the independent variable.
    y_col (str): The name of the column to be used as the dependent variable.

    Returns:
    pandas.DataFrame: The DataFrame with the added 'predicted' column.
    """
    # Extract the data for the two variables
    x = df[x_col]
    y = df[y_col]
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Calculate the predicted values
    df['predicted'] = slope * x + intercept
    
    return df

# Example usage:
# df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 4, 5]})
# df = task_func(df, 'x', 'y')
# print(df)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'var1': np.random.randn(10),
                           'var2': np.random.randn(10)})
        df = task_func(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 10)
        self.assertEqual(len(df.columns), 3)
    def test_case_2(self):
        df = pd.DataFrame({'var1': [1, 2, 3, 4, 5],
                            'var2': [1, 2, 3, 4, 5]})
        df = task_func(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 5)
        self.assertEqual(len(df.columns), 3)
        self.assertTrue(np.all(df['predicted'] == df['var2']))
    
    def test_case_3(self):
        df = pd.DataFrame({'var1': [1, 2, 3, 4, 5],
                            'var2': [5, 4, 3, 2, 1]})
        df = task_func(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 5)
        self.assertEqual(len(df.columns), 3)
        self.assertTrue(np.all(df['predicted'] == df['var2']))
    def test_case_4(self):
        df = pd.DataFrame({'var1': [1, 2, 3, 4, 5],
                            'var2': [1, 1, 1, 1, 1]})
        df = task_func(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 5)
        self.assertEqual(len(df.columns), 3)
        self.assertTrue(np.all(df['predicted'] == df['var2']))
    def test_case_5(self):
        df = pd.DataFrame({'var1': [0, 1, 2, 3, 4, 5],
                            'var2': [1, 1, 1, 1, 1, 1]})
        df = task_func(df)
        self.assertTrue('predicted' in df.columns)
        self.assertEqual(len(df), 6)
        self.assertEqual(len(df.columns), 3)
        self.assertTrue(np.all(df['predicted'] == df['var2']))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)