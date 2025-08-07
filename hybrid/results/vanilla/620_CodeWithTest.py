import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)

def task_func(L):
    # Calculate the number of rows and columns by multiplying pairs of integers
    rows = 1
    cols = 1
    for sublist in L:
        if len(sublist) == 2:
            rows *= sublist[0]
            cols *= sublist[1]
    
    # Generate random integers within the specified range
    data = np.random.randint(RANGE[0], RANGE[1], size=(rows, cols))
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame(data)
    
    return df

# Example usage:
# L = [[2, 3], [4, 5]]
# df = task_func(L)
# print(df)
import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        result = task_func([[2, 3], [5, 6]])
        self.assertEqual(result.shape, (2*3, 5*6))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
    def test_case_2(self):
        result = task_func([[1, 1], [1, 1]])
        self.assertEqual(result.shape, (1*1, 1*1))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
    def test_case_3(self):
        result = task_func([[4, 5], [2, 3]])
        self.assertEqual(result.shape, (4*5, 2*3))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
    def test_case_4(self):
        result = task_func([[3, 2], [6, 5]])
        self.assertEqual(result.shape, (3*2, 6*5))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())
    def test_case_5(self):
        result = task_func([[7, 8], [1, 2]])
        self.assertEqual(result.shape, (7*8, 1*2))
        self.assertTrue((result.values >= 1).all())
        self.assertTrue((result.values <= 100).all())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)