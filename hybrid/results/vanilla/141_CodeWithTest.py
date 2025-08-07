import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    # Validate the number of rows
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("The 'rows' parameter must be a positive integer greater than 0.")
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random numbers between 1 and 100
    data = np.random.randint(1, 101, size=(rows, len(columns)))
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=columns)
    
    # Calculate the mean and median for each column
    stats_dict = {}
    for column in columns:
        mean_value = df[column].mean()
        median_value = df[column].median()
        stats_dict[column] = {
            'mean': mean_value,
            'median': median_value
        }
    
    return df, stats_dict

# Example usage:
# df, stats = task_func(10)
# print(df)
# print(stats)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_dataframe_structure(self):
        df, _ = task_func(10)
        self.assertEqual(df.shape, (10, 6))  # 10 rows, 6 columns
    def test_invalid_rows_input_negative(self):
        with self.assertRaises(ValueError):
            task_func(-1)
    def test_invalid_rows_input_zero(self):
        with self.assertRaises(ValueError):
            task_func(0)
    def test_invalid_rows_type(self):
        with self.assertRaises(ValueError):
            task_func("five")
    def test_stats_calculation(self):
        _, stats = task_func(10)
        for col_stats in stats.values():
            self.assertIn('mean', col_stats)
            self.assertIn('median', col_stats)
            
    def test_specific_stats_values(self):
        df, stats = task_func(10)
        for col in df.columns:
            expected_mean = df[col].mean()
            expected_median = df[col].median()
            self.assertAlmostEqual(stats[col]['mean'], expected_mean)
            self.assertAlmostEqual(stats[col]['median'], expected_median)
    def test_reproducibility_with_seed(self):
        df1, _ = task_func(10, seed=123)
        df2, _ = task_func(10, seed=123)
        pd.testing.assert_frame_equal(df1, df2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)