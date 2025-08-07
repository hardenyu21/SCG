import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        return 0, 0
    
    # Convert lists in the DataFrame into separate columns
    # Assuming the DataFrame has a column named 'numbers' containing lists
    df_expanded = df.drop('numbers', axis=1).join(df['numbers'].apply(pd.Series))
    
    # Perform PCA
    pca = PCA()
    principal_components = pca.fit_transform(df_expanded)
    
    # Get the explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Plot the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio)
    ax.set_title("Explained Variance Ratio of Principal Components")
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    
    # Return the explained variance ratio and the Axes object
    return explained_variance_ratio, ax
import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_return_types(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        variance_ratio, plot = task_func(df)
        self.assertIsInstance(variance_ratio, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
    def test_known_input_output(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        variance_ratio, plot = task_func(df)
        self.assertIsInstance(variance_ratio, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
    def test_empty_dataframe(self):
        empty_df = pd.DataFrame()
        variance_ratio, _ = task_func(empty_df)
        self.assertEqual(variance_ratio, 0)
    def test_single_row_dataframe(self):
        single_row_df = pd.DataFrame([['2021-01-01', [8, 10, 12]]], columns=['Date', 'Value'])
        variance_ratio, _ = task_func(single_row_df)
        self.assertEqual(len(variance_ratio), 1)
    def test_plot_attributes(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        _, ax = task_func(df)
        self.assertEqual(ax.get_title(), 'Explained Variance Ratio of Principal Components')
        self.assertEqual(ax.get_xlabel(), 'Principal Component')
        self.assertEqual(ax.get_ylabel(), 'Explained Variance Ratio')
    def test_plot_explained_variance_ratio(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        variance_ratio, ax = task_func(df)
        bar_heights = [rect.get_height() for rect in ax.patches]
        self.assertListEqual(bar_heights, list(variance_ratio))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)