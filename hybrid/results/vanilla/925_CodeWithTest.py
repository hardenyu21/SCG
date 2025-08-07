import pandas as pd
import numpy as np

def task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a DataFrame with random integers between 1 and 100
    df = pd.DataFrame(np.random.randint(1, 101, size=(data_size, len(column_names))), columns=column_names)
    
    # Replace all values less than 10 with -1
    df[df < 10] = -1
    
    return df

# Example usage:
# df = task_func()
# print(df)
import unittest
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        df = task_func(seed=42)
        self.assertEqual(df.shape, (1000, 5))
        # Check that there are no values < 10 except -1
        condition = ((df >= 10) | (df == -1)).all().all()
        self.assertTrue(condition, "DataFrame contains values less than 10 that were not replaced with -1")
    def test_custom_data_size_and_columns(self):
        df = task_func(data_size=10, column_names=['X', 'Y'], seed=55)
        self.assertEqual(df.shape, (10, 2))
        # Check that there are no values < 10 except -1
        condition = ((df >= 10) | (df == -1)).all().all()
        self.assertTrue(condition, "DataFrame contains values less than 10 that were not replaced with -1")
    def test_correct_replacement_of_values(self):
        df = task_func(data_size=100, seed=0)
        self.assertTrue(((df >= 10) | (df == -1)).all().all(), "Not all values less than 10 were replaced with -1")
    
    def test_correct_dataframe_dimensions(self):
        rows, columns = 50, 3
        df = task_func(data_size=rows, column_names=['P', 'Q', 'R'], seed=1)
        self.assertEqual(df.shape, (rows, columns), "DataFrame dimensions are incorrect")
    
    def test_with_minimum_data_size(self):
        df = task_func(data_size=1, column_names=['Single'], seed=2)
        self.assertEqual(df.shape, (1, 1), "DataFrame does not handle minimum data size correctly")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)