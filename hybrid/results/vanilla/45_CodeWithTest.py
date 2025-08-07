import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Fill missing values with the column's average
    numeric_df_filled = numeric_df.fillna(numeric_df.mean())
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(numeric_df_filled)
    
    # Create a DataFrame with the first two principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['Component 1', 'Component 2'])
    
    # Plot the scatter plot
    plt.figure(figsize=(8, 6))
    ax = sns.scatterplot(x='Component 1', y='Component 2', data=principal_df)
    ax.set_xlabel('Component 1')
    ax.set_ylabel('Component 2')
    plt.title('PCA of Dataset')
    
    # Return the DataFrame and the Axes object
    return principal_df, ax

# Example usage:
# df = pd.read_csv('your_dataset.csv')
# principal_df, ax = task_func(df)
# plt.show()
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        df = pd.DataFrame(
            [[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"]
        )
        principalDf, ax = task_func(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (3, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")
    def test_case_2(self):
        df = pd.DataFrame(
            {
                "A": [1, 2.5, 3, 4.5, 5],
                "B": [5, 4.5, np.nan, 2, 1.5],
                "C": [2.5, 3, 4, 5.5, 6],
                "categoral_1": ["A", "B", "B", "B", "A"],
                "categoral_2": ["0", "1", "1", "0", "1"],
            }
        )
        principalDf, ax = task_func(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (5, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")
    def test_case_3(self):
        df = pd.DataFrame(
            {
                "col1": [None, 17, 11, None],
                "col2": [0, 4, 15, 27],
                "col3": [7, 9, 3, 8],
            }
        )
        principalDf, ax = task_func(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (4, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")
    def test_case_4(self):
        df = pd.DataFrame(
            {
                "c1": [np.nan] * 9 + [10],
                "c2": [np.nan] * 8 + [20, 30],
                "c3": [np.nan] * 7 + [40, 50, 60],
            }
        )
        principalDf, ax = task_func(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (10, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")
    def test_case_5(self):
        df = pd.DataFrame({"c1": [1] * 10, "c2": [2] * 10, "c3": [3] * 10})
        principalDf, ax = task_func(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (10, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)