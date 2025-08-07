import numpy as np
import pandas as pd

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random values in the range [0, 1) with the specified number of rows and columns
    data = np.random.rand(rows, len(columns))
    
    # Create a DataFrame with the generated data and the specified columns
    df = pd.DataFrame(data, columns=columns)
    
    # Shuffle the columns
    shuffled_columns = np.random.permutation(columns)
    
    # Return the DataFrame with shuffled columns
    return df[shuffled_columns]

# Example usage:
# df = task_func(5)
# print(df)
import unittest
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case - data and format correctness
        df = task_func(10, seed=0)
        default_columns = ["A", "B", "C", "D", "E"]
        self.assertEqual(df.shape, (10, 5))
        for column in default_columns:
            self.assertEqual(df.dtypes[column], np.float64)
        self.assertEqual(len(set(df.columns)), len(default_columns))
    def test_case_2(self):
        # Test custom columns
        custom_columns = ["X", "Y", "Z"]
        df = task_func(5, columns=custom_columns, seed=0)
        self.assertTrue(all(column in custom_columns for column in df.columns))
        # assert first 2 rows data
        self.assertEqual(set(df.iloc[0].tolist()), {0.5488135039273248, 0.7151893663724195, 0.6027633760716439})
        
    def test_case_3(self):
        # Test custom rows
        for n_rows in [1, 10, 50]:
            df = task_func(n_rows)
            self.assertEqual(len(df), n_rows)
    def test_case_4(self):
        df = task_func(5, seed=42)
        self.assertEqual(set(df.iloc[0].tolist()), {0.3745401188473625, 0.9507143064099162, 0.7319939418114051, 0.5986584841970366, 0.15601864044243652})
    def test_case_5(self):
        # Test handling edge cases - negative rows
        with self.assertRaises(ValueError):
            task_func(-1)
    def test_case_6(self):
        # Test handling empty columns
        df = task_func(5, columns=[])
        self.assertTrue(df.empty)
    def test_case_7(self):
        # Test handling duplicate columns
        df = task_func(5, columns=["A", "A", "B", "B", "C"], seed=0)
        self.assertEqual(len(df.columns), 3)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)