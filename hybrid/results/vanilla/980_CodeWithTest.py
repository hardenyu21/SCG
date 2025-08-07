import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Check if there are no numeric columns
    if numeric_df.empty:
        raise ValueError("No numeric columns are present in the DataFrame.")
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(numeric_df)
    standardized_df = pd.DataFrame(standardized_data, columns=numeric_df.columns, index=numeric_df.index)
    
    # Compute the correlation matrix
    corr_matrix = standardized_df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.close()  # Close the plot to prevent it from displaying immediately
    
    return standardized_df, heatmap.get_figure()
import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case with integer values
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        standardized_df, fig = task_func(df)
        self.assertTrue(np.allclose(standardized_df.mean(), 0))
        self.assertTrue(np.allclose(standardized_df.std(ddof=0), 1))
        self.assertTrue(isinstance(fig, plt.Figure))
    def test_case_2(self):
        # Test case with float values
        df = pd.DataFrame({"X": [1.1, 2.2, 3.3], "Y": [4.4, 5.5, 6.6]})
        standardized_df, fig = task_func(df)
        self.assertTrue(np.allclose(standardized_df.mean(), 0))
        self.assertTrue(np.allclose(standardized_df.std(ddof=0), 1))
        self.assertTrue(isinstance(fig, plt.Figure))
    def test_case_3(self):
        # Test case with negative values
        df = pd.DataFrame({"A": [-1, -2, -3], "B": [-4, -5, -6]})
        standardized_df, fig = task_func(df)
        self.assertTrue(np.allclose(standardized_df.mean(), 0))
        self.assertTrue(np.allclose(standardized_df.std(ddof=0), 1))
        self.assertTrue(isinstance(fig, plt.Figure))
    def test_case_4(self):
        # Test case with single column
        df = pd.DataFrame({"A": [1, 2, 3]})
        standardized_df, fig = task_func(df)
        self.assertTrue(np.allclose(standardized_df.mean(), 0))
        self.assertTrue(np.allclose(standardized_df.std(ddof=0), 1))
        self.assertTrue(isinstance(fig, plt.Figure))
    def test_case_5(self):
        # Test proper exception handling - no numeric columns
        df = pd.DataFrame({"A": ["apple", "banana", "cherry"]})
        with self.assertRaises(ValueError):
            task_func(df)
    def test_case_6(self):
        # Test proper exception handling - empty dataframe
        df = pd.DataFrame()
        with self.assertRaises(ValueError):
            task_func(df)
    def test_case_7(self):
        # Test ignoring non-numeric columns
        df = pd.DataFrame({"A": [1, 2, 3], "B": ["x", "y", "z"], "C": [4.5, 5.5, 6.5]})
        standardized_df, fig = task_func(df)
        self.assertTrue("B" in standardized_df.columns)
        self.assertTrue(np.allclose(standardized_df[["A", "C"]].mean(), 0))
        self.assertTrue(np.allclose(standardized_df[["A", "C"]].std(ddof=0), 1))
        self.assertIsInstance(fig, plt.Figure)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)