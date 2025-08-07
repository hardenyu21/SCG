import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(data_matrix):
    # Calculate Z-scores for each row
    z_scores = data_matrix.apply(zscore, axis=1)
    
    # Calculate the mean of Z-scores for each row
    z_scores['Mean'] = z_scores.mean(axis=1)
    
    # Create a correlation matrix of the Z-scores
    corr_matrix = z_scores.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', cbar=True)
    plt.title('Correlation Matrix of Z-scores')
    plt.show()
    
    return z_scores, ax

# Example usage:
# data_matrix = pd.DataFrame({
#     'Feature 1': [1, 2, 3, 4],
#     'Feature 2': [4, 3, 2, 1],
#     'Feature 3': [2, 3, 4, 5]
# })
# z_scores_df, heatmap_ax = task_func(data_matrix)
import unittest
import numpy as np
import matplotlib
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        df, ax = task_func(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)
    def test_case_2(self):
        data = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        df, ax = task_func(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)
    def test_case_3(self):
        data = np.array([[3, 5, 7, 1000], [200, 5, 7, 1], [1, -9, 14, 700]])
        df, ax = task_func(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)
    def test_case_4(self):
        data = np.array(
            [
                [1, 2, 3, 4, 5, 4, 3, 2, 1],
            ]
        )
        df, ax = task_func(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)
    def test_case_5(self):
        data = np.array([[1], [1], [1]])
        df, ax = task_func(data)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue(isinstance(ax, matplotlib.axes.Axes))
        np.testing.assert_array_equal(
            df.loc[:, [col for col in df.columns if col.startswith("Feature")]].values,
            zscore(data, axis=1),
        )
        self.assertTrue("Mean" in df.columns)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)