import seaborn as sns
import numpy as np
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the DataFrame contains non-numeric data types
    if not all(np.issubdtype(dtype, np.number) for dtype in df.dtypes):
        raise TypeError("The DataFrame contains non-numeric data types.")
    
    # Calculate the covariance matrix
    covariance_df = df.cov()
    
    # Generate the pair plot
    pair_plot = sns.pairplot(df)
    
    return covariance_df, pair_plot
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_covariance_one(self):
        """Test basic case with expected covariance of 1.0"""
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
        covariance_df, _ = task_func(df)
        self.assertTrue((covariance_df == 1).all().all())
    def test_identical_values_dataframe(self):
        """Test DataFrame where all rows have identical values."""
        df = pd.DataFrame({"A": [1, 1, 1], "B": [2, 2, 2]})
        covariance_df, _ = task_func(df)
        self.assertTrue((covariance_df == 0).all().all())
    def test_with_empty_dataframe(self):
        """Test handling empty input (should raise error)."""
        df = pd.DataFrame()
        with self.assertRaises(ValueError):
            task_func(df)
    def test_with_non_numeric_dataframe(self):
        """Test handling unsupported data types."""
        df = pd.DataFrame({"A": ["a", "b", "c"], "B": ["d", "e", "f"]})
        with self.assertRaises(TypeError):
            task_func(df)
    def test_plot_attributes(self):
        """Test plot attributes."""
        df = pd.DataFrame({"X": [10, 20, 30], "Y": [15, 25, 35]})
        _, pair_plot = task_func(df)
        self.assertIsInstance(pair_plot, sns.axisgrid.PairGrid)
        self.assertEqual(len(pair_plot.axes), 2)  # Should have 2x2 grid for pair plot
    def test_single_column_dataframe(self):
        """Test handling of DataFrame with a single numeric column."""
        df = pd.DataFrame({"A": [1, 2, 3]})
        covariance_df, _ = task_func(df)
        self.assertEqual(covariance_df.loc["A"].item(), 1.0)
        self.assertEqual(covariance_df.shape, (1, 1))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)