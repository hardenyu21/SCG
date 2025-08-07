import numpy as np
from scipy import stats

def task_func(df, column, alpha):
    # Extract the column data as a numpy array
    data = df[column].values
    
    # Perform the Shapiro-Wilk test for normality
    stat, p_value = stats.shapiro(data)
    
    # Determine if the data is normally distributed
    is_normal = p_value > alpha
    
    return is_normal
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
    def test_case_1(self):
        df = pd.DataFrame({'Value': np.random.normal(0, 1, 1000)})
        self.assertTrue(task_func(df, 'Value', 0.05))
    def test_case_2(self):
        df = pd.DataFrame({'Value': np.random.uniform(0, 1, 1000)})
        self.assertFalse(task_func(df, 'Value', 0.05))
    def test_case_3(self):
        df = pd.DataFrame({'Value': np.random.exponential(1, 1000)})
        self.assertFalse(task_func(df, 'Value', 0.05))
    def test_case_4(self):
        df = pd.DataFrame({'Value': np.random.lognormal(0, 1, 1000)})
        self.assertFalse(task_func(df, 'Value', 0.05))
    def test_case_5(self):
        df = pd.DataFrame({'Value': np.random.chisquare(1, 1000)})
        self.assertFalse(task_func(df, 'Value', 0.05))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)