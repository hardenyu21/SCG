import numpy as np
import pandas as pd
import random

def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    np.random.seed(seed)
    
    # Generate a matrix of random integers within the specified range
    matrix = np.random.randint(min_val, max_val + 1, size=(rows, cols))
    
    # Convert the matrix into a pandas DataFrame
    df = pd.DataFrame(matrix)
    
    return df

# Example usage:
# df = task_func(4, 3, 10, 50, 42)
# print(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iloc[:, 0].tolist(), [49, 53, 33])
        self.assertEqual(df.iloc[:, 1].tolist(), [97, 5, 65])
        
    def test_case_2(self):
        df = task_func(rows=5, cols=4)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iloc[:, 0].tolist(), [49, 33, 38, 27, 17])
        self.assertEqual(df.iloc[:, 1].tolist(), [97, 65, 61, 64, 96])
        self.assertEqual(df.iloc[:, 2].tolist(), [53, 62, 45, 17, 12])
    def test_case_3(self):
        df = task_func(min_val=10, max_val=20)
        self.assertEqual(df.iloc[:, 0].tolist(), [16, 10, 18])
        self.assertEqual(df.iloc[:, 1].tolist(), [16, 14, 17])
        
    def test_case_4(self):
        df = task_func(min_val=50, max_val=50)
        self.assertEqual(df.iloc[:, 0].tolist(), [50, 50, 50])
        self.assertEqual(df.iloc[:, 1].tolist(), [50, 50, 50])
    def test_case_5(self):
        df = task_func(rows=0, cols=2)
        self.assertTrue(df.empty)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)