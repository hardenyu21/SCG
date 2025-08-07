import numpy as np
import pandas as pd

def task_func(rows, columns, seed=None):
    """
    Generates a DataFrame with random values within a specified range.

    Parameters:
    - rows (int): Number of rows in the DataFrame.
    - columns (int): Number of columns in the DataFrame.
    - seed (int, optional): Random seed for reproducibility. Defaults to None.

    Returns:
    - DataFrame: A Pandas DataFrame containing the generated random values.
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random values between 0 and 1
    random_values = np.random.rand(rows, columns)
    
    # Create a DataFrame from the random values
    df = pd.DataFrame(random_values)
    
    return df

# Example usage:
# df = task_func(5, 3, seed=42)
# print(df)
import unittest
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.seed = 42
    def test_case_1(self):
        df = task_func(3, 2, seed=self.seed)
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())
        
    def test_case_2(self):
        df = task_func(5, 5, seed=self.seed)
        self.assertEqual(df.shape, (5, 5))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())
        
    def test_case_3(self):
        df = task_func(1, 1, seed=self.seed)
        self.assertEqual(df.shape, (1, 1))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())
        
    def test_case_4(self):
        df = task_func(4, 3, seed=self.seed)
        self.assertEqual(df.shape, (4, 3))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())
        
    def test_case_5(self):
        df = task_func(2, 2, seed=self.seed)
        self.assertEqual(df.shape, (2, 2))
        self.assertTrue((df >= 0).all().all())
        self.assertTrue((df <= 1).all().all())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)