import numpy as np
import pandas as pd
from scipy import stats

def task_func(df):
    """
    Perform the Shapiro-Wilk test for normality on each column of the DataFrame.

    Parameters:
    df (pd.DataFrame): A DataFrame with numeric values.

    Returns:
    dict: A dictionary with column names as keys and p-values from the Shapiro-Wilk test as values.
    """
    results = {}
    for column in df.columns:
        # Perform the Shapiro-Wilk test
        stat, p_value = stats.shapiro(df[column])
        # Store the p-value in the results dictionary
        results[column] = p_value
    return results

# Example usage:
# df = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])
# p_values = task_func(df)
# print(p_values)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
    
    def test_case_1(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        p_values = task_func(df)
        self.assertEqual(len(p_values), 2)
        self.assertTrue('a' in p_values)
        self.assertTrue('b' in p_values)
        self.assertTrue(p_values['a'] > 0.05)
        self.assertTrue(p_values['b'] > 0.05)
    def test_case_2(self):
        df = pd.DataFrame({'a': [-1, 0, 1], 'b': [4, 5, 6]})
        p_values = task_func(df)
        self.assertEqual(len(p_values), 2)
        self.assertTrue('a' in p_values)
        self.assertTrue('b' in p_values)
        self.assertTrue(p_values['a'] > 0.05)
        self.assertTrue(p_values['b'] > 0.05)
    def test_case_3(self):
        df = pd.DataFrame(np.random.normal(size=(100, 5)))
        p_values = task_func(df)
        self.assertEqual(len(p_values), 5)
        for col in df.columns:
            self.assertTrue(col in p_values)
            self.assertTrue(p_values[col] > 0.05)
    def test_case_4(self):
        df = pd.DataFrame(np.random.normal(size=(100, 5)))
        df['a'] = np.random.uniform(size=100)
        p_values = task_func(df)
        self.assertEqual(len(p_values), 6)
        for col in df.columns:
            self.assertTrue(col in p_values)
            if col == 'a':
                self.assertTrue(p_values[col] < 0.05)
            else:
                self.assertTrue(p_values[col] > 0.05)
    def test_case_5(self):
        df = pd.DataFrame(np.random.normal(size=(100, 5)))
        df['a'] = np.random.uniform(size=100)
        df['b'] = np.random.uniform(size=100)
        p_values = task_func(df)
        self.assertEqual(len(p_values), 7)
        for col in df.columns:
            self.assertTrue(col in p_values)
            if col in ['a', 'b']:
                self.assertTrue(p_values[col] < 0.05)
            else:
                self.assertTrue(p_values[col] > 0.05)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)