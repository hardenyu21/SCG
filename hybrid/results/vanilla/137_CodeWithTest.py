import pandas as pd
from scipy.stats import skew

def task_func(df):
    # Check if the input is a DataFrame and has at least one column
    if not isinstance(df, pd.DataFrame) or df.shape[1] == 0:
        raise ValueError("If the input is not a DataFrame or has no columns.")
    
    # Calculate the skewness of the last column
    last_column_skewness = skew(df.iloc[:, -1])
    
    return last_column_skewness
import unittest
import numpy as np
import pandas as pd 
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    def test_skewness_calculation(self):
        skewness = task_func(self.df)
        # print(skewness)
        self.assertIsInstance(skewness, float)
        self.assertAlmostEqual(-0.1670862308059806, skewness)
    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            task_func("not a dataframe")
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())
    def test_with_nan_values(self):
        self.df.iloc[::10, -1] = np.nan
        skewness = task_func(self.df)
        self.assertIsInstance(skewness, float)
    def test_single_column_df(self):
        df_single_col = pd.DataFrame(self.df.iloc[:, 0])
        skewness = task_func(df_single_col)
        self.assertIsInstance(skewness, float)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)