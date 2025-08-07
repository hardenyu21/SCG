import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(df, features):
    """
    Standardizes the specified features in the DataFrame using StandardScaler.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    features (list): A list of column names to be standardized.

    Returns:
    pandas.DataFrame: The DataFrame with the standardized features.
    """
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the specified features
    df[features] = scaler.fit_transform(df[features])
    
    return df
import unittest
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        np.random.seed(42)
    def test_case_1(self):
        df = pd.DataFrame(np.random.randn(10, 3), columns=['a', 'b', 'c'])
        df = task_func(df, ['a', 'b'])
        self.assertEqual(df.shape, (10, 3))
        self.assertTrue('a' in df.columns)
        self.assertTrue('b' in df.columns)
        self.assertTrue('c' in df.columns)
        self.assertTrue(np.all(df['a'] >= -5) and np.all(df['a'] <= 5))
        self.assertTrue(np.all(df['b'] >= -5) and np.all(df['b'] <= 5))
        self.assertTrue(np.all(df['c'] >= -5) and np.all(df['c'] <= 5))
    def test_case_2(self):
        df = pd.DataFrame({'a': [0, 0, 0], 'b': [0, 0, 0], 'c': [0, 0, 0]})
        df = task_func(df, ['a', 'b'])
        self.assertEqual(df.shape, (3, 3))
        self.assertTrue('a' in df.columns)
        self.assertTrue('b' in df.columns)
        self.assertTrue('c' in df.columns)
        self.assertTrue(np.all(df['a'] == 0))
        self.assertTrue(np.all(df['b'] == 0))
        self.assertTrue(np.all(df['c'] == 0))
    def test_case_3(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        df = task_func(df, ['a', 'b'])
        self.assertEqual(df.shape, (3, 3))
        self.assertTrue('a' in df.columns)
        self.assertTrue('b' in df.columns)
        self.assertTrue('c' in df.columns)
        self.assertTrue(np.all(df['a'] >= -3) and np.all(df['a'] <= 3))
        self.assertTrue(np.all(df['b'] >= -3) and np.all(df['b'] <= 3))
        self.assertTrue(np.all(df['c'] == [7, 8, 9]))
    def test_case_4(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        df = task_func(df, ['c'])
        self.assertEqual(df.shape, (3, 3))
        self.assertTrue('a' in df.columns)
        self.assertTrue('b' in df.columns)
        self.assertTrue('c' in df.columns)
        self.assertTrue(np.all(df['a'] == [1, 2, 3]))
        self.assertTrue(np.all(df['b'] == [4, 5, 6]))
        self.assertTrue(np.all(df['c'] >= -3) and np.all(df['c'] <= 3))
    def test_case_5(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        df = task_func(df, [])
        self.assertEqual(df.shape, (3, 3))
        self.assertTrue('a' in df.columns)
        self.assertTrue('b' in df.columns)
        self.assertTrue('c' in df.columns)
        self.assertTrue(np.all(df['a'] == [1, 2, 3]))
        self.assertTrue(np.all(df['b'] == [4, 5, 6]))
        self.assertTrue(np.all(df['c'] == [7, 8, 9]))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)