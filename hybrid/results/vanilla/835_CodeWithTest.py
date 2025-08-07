import numpy as np
import pandas as pd

def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random integer values between 0 and 100
    data = np.random.randint(0, 101, size=(n_rows, len(columns)))
    
    # Create a DataFrame with the generated data and specified columns
    df = pd.DataFrame(data, columns=columns)
    
    # Remove columns based on the provided indexes
    df = df.drop(df.columns[remove_cols], axis=1)
    
    return df

# Example usage
df = task_func(3, [1, 3], columns=['test', 'rem1', 'apple', 'remove'], random_seed=12)
print(df)
import unittest
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = task_func(5, [1, 3], random_seed=1)
        expected = pd.DataFrame({
            'A': {0: 37, 1: 5, 2: 76, 3: 20, 4: 29},
            'C': {0: 72, 1: 64, 2: 6, 3: 84, 4: 50},
            'E': {0: 75, 1: 1, 2: 50, 3: 28, 4: 87}
        })
        pd.testing.assert_frame_equal(df, expected, check_dtype=False)
    def test_case_2(self):
        df = task_func(10, [], columns=['X', 'Y', 'Z'], random_seed=12)
        expected = pd.DataFrame({
            'X': {0: 75, 1: 2, 2: 76, 3: 49, 4: 13, 5: 75, 6: 76, 7: 89, 8: 35, 9: 63},
            'Y': {0: 27, 1: 3, 2: 48, 3: 52, 4: 89, 5: 74, 6: 13, 7: 35, 8: 33, 9: 96},
            'Z': {0: 6, 1: 67, 2: 22, 3: 5, 4: 34, 5: 0, 6: 82, 7: 62, 8: 30, 9: 18}
        })
        pd.testing.assert_frame_equal(df, expected, check_dtype=False)
    def test_case_3(self):
        df = task_func(0, remove_cols=[], random_seed=42)
        expected = pd.DataFrame(
            {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}}
        )
        pd.testing.assert_frame_equal(df, expected, check_dtype=False, check_index_type=False)
    def test_case_4(self):
        df1 = task_func(10, [], random_seed=12)
        df2 = task_func(10, [], random_seed=12)
        pd.testing.assert_frame_equal(df1, df2, check_dtype=False, check_index_type=False)
    def test_case_5(self):
        df = task_func(6, [0, 1, 2, 3, 4], random_seed=1)
        self.assertEqual(list(df.columns), [])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)