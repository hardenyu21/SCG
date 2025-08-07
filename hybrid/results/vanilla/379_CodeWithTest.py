import pandas as pd
import numpy as np

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length):
    # Generate random data
    data = np.random.rand(length, len(COLUMNS))
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Record the data (for demonstration, we'll just print it)
    print(df)
    
    # Return the DataFrame
    return df

# Example usage
df = task_func(10)
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Testing basic functionality
        np.random.seed(0)
        df = task_func(5)
        self.assertIsInstance(df, pd.DataFrame, "Output should be a DataFrame.")
        self.assertEqual(df.shape, (5, 5), "DataFrame shape mismatch.")
        
    def test_case_2(self):
        # Testing custom columns
        np.random.seed(0)
        custom_columns = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
        df = task_func(3)
        self.assertListEqual(list(df.columns), custom_columns, "Column names mismatch.")
        
    def test_case_3(self):
        # Testing return plot
        np.random.seed(0)
        df = task_func(4)
        self.assertIsInstance(df, pd.DataFrame, "Output should be a DataFrame.")
        
    def test_case_4(self):
        # Testing data range
        np.random.seed(0)
        df = task_func(10)
        self.assertTrue((df.values >= 0).all() and (df.values < 100).all(), "Data values should be between 0 and 99.")
        
    def test_case_5(self):
        # Testing default columns
        np.random.seed(0)
        df = task_func(7)
        default_columns = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
        self.assertListEqual(list(df.columns), default_columns, "Default column names mismatch.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)