import pandas as pd
from statsmodels.tsa.stattools import adfuller

def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df[column_b] > 50) & (df[column_c] == 900)]
    
    # Extract the relevant column after filtering
    filtered_column_a = filtered_df[column_a]
    
    # Check if column_a is empty or has constant values
    if filtered_column_a.empty or filtered_column_a.nunique() == 1:
        return True
    
    # Perform the Augmented Dickey-Fuller test
    adf_result = adfuller(filtered_column_a)
    p_value = adf_result[1]
    
    # Determine if the data is stationary
    return p_value < 0.05
import unittest
import os
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create DataFrame in setUp for test isolation
        self.data = pd.DataFrame({
            'A': list(range(100)),
            'B': [x * 2 for x in range(100)],
            'C': [900 if x % 2 == 0 else 800 for x in range(100)]
        })
    def test_constant_value(self):
        # All values in column A are constant after filtering
        self.data['A'] = 5
        result = task_func(self.data, 'A', 'B', 'C')
        self.assertTrue(result, "Should be True as data is constant.")
    def test_empty_after_filter(self):
        # After filtering, no rows remain
        result = task_func(self.data[self.data['B'] > 1000], 'A', 'B', 'C')
        self.assertTrue(result, "Should be True as no data remains after filter.")
    def test_non_stationary_data(self):
        # Test a clearly non-stationary dataset
        result = task_func(self.data, 'A', 'B', 'C')
        self.assertFalse(result, "Should be False as data is non-stationary.")
    def test_stationary_data(self):
        # Test a stationary dataset
        self.data['A'] = 5
        result = task_func(self.data, 'A', 'B', 'C')
        self.assertTrue(result, "Should be True as data is stationary.")
    def test_edge_case_small_dataset(self):
        # Test a very small dataset
        small_data = pd.DataFrame({
            'A': [1, 1],
            'B': [60, 70],
            'C': [900, 900]
        })
        result = task_func(small_data, 'A', 'B', 'C')
        self.assertTrue(result, "Should be True due to small dataset size or no variation.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)