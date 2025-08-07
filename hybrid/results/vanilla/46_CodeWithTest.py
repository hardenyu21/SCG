from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace missing values with the column's average
    df_filled = df.fillna(df.mean())
    
    # Calculate Z-scores for numeric columns
    z_scores_df = df_filled.apply(zscore)
    
    # Initialize a list to store Axes objects
    axes_list = []
    
    # Plot histograms for each numeric column
    for column in z_scores_df.columns:
        fig, ax = plt.subplots()
        z_scores_df[column].hist(bins=10, ax=ax)
        ax.set_title(f'Histogram of Z-scores for {column}')
        ax.set_xlabel('Z-score')
        ax.set_ylabel('Frequency')
        axes_list.append(ax)
    
    # Return the DataFrame with Z-scores and the list of Axes objects
    return z_scores_df, axes_list
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        df = pd.DataFrame(
            {
                "col1": [1, 7, 3],
                "col2": [4, 5, 7],
                "col3": [None, None, None],
            }
        )
        zscores, plots = task_func(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 3)
    def test_case_2(self):
        df = pd.DataFrame(
            {
                "col1": [None, None, 3],
                "col2": [None, 5, 7],
                "col3": [8, 6, 4],
            }
        )
        zscores, plots = task_func(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 3)
    def test_case_3(self):
        df = pd.DataFrame(
            {
                "col1": [None, 17, 11, None],
                "col2": [0, 4, 15, 27],
                "col3": [7, 9, 3, 8],
            }
        )
        # Expected solutions
        expected_df = df.copy()
        expected_df = expected_df.fillna(expected_df.mean(axis=0))
        expected_df = expected_df.apply(zscore)
        # Function execution
        zscores, plots = task_func(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 3)
        pd.testing.assert_frame_equal(zscores, expected_df)
    def test_case_4(self):
        df = pd.DataFrame(
            {
                "col1": [1, 7, 3, None],
                "col2": [4, 5, 7, 2],
            }
        )
        zscores, plots = task_func(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 2)
    def test_case_5(self):
        df = pd.DataFrame(
            {
                "col1": [1, 2, 3, 4, 5],
                "col2": [None, None, None, None, None],
            }
        )
        zscores, plots = task_func(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 2)
    def test_case_6(self):
        df = pd.DataFrame(
            {
                "A": [np.nan, np.nan, np.nan],
                "B": [np.nan, np.nan, np.nan],
                "C": [np.nan, np.nan, np.nan],
            }
        )
        zscores, plots = task_func(df)
        self.assertTrue(zscores.isnull().all().all())
        self.assertEqual(len(plots[0]), 3)
    def test_case_7(self):
        df = pd.DataFrame(
            {
                "A": [1, 2.5, 3, 4.5, 5],
                "B": [5, 4.5, np.nan, 2, 1.5],
                "C": [2.5, 3, 4, 5.5, 6],
            }
        )
        zscores, plots = task_func(df)
        self.assertAlmostEqual(zscores.mean().mean(), 0.0, places=6)
        self.assertEqual(len(plots[0]), 3)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)