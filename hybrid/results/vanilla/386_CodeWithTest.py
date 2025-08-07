import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length, min_value=0, max_value=100):
    # Generate random data within the specified range
    data = np.random.uniform(min_value, max_value, size=(length, len(COLUMNS)))
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Calculate the cumulative distribution function (CDF) for each column
    cdf_df = df.rank(method='average', pct=True)
    
    return cdf_df

# Example usage
length = 10
cdf_df = task_func(length)
print(cdf_df)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        np.random.seed(0)
        df = task_func(100, 0, 1)
        self.assertEqual(df.shape[0], 1)
        self.assertEqual(list(df.columns), ['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
    def test_case_2(self):
        np.random.seed(0)
        min_value = 0
        max_value = 1
        length = 10
        cdf = task_func(length, min_value, max_value)
        self.assertEqual(cdf.iloc[0]['Column1'], 10)
    def test_case_3(self):
        np.random.seed(0)
        df = task_func(100)
        #self.assertEqual(df.shape[0], 100)
        self.assertEqual(list(df.columns), ['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
    def test_case_4(self):
        np.random.seed(0)
        df = task_func(100, 50, 100)
        self.assertEqual(list(df.columns), ['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
        for column in df.columns:
            self.assertTrue(all(df[column].diff().dropna() >= 0))
    def test_case_5(self):
        np.random.seed(0)
        df  = task_func(0)
        self.assertEqual(df.shape[0], 0)
        self.assertEqual(list(df.columns), ['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)