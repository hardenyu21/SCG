import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def task_func(data_matrix):
    # Calculate the skewness for each row
    skewness_values = data_matrix.apply(lambda row: skew(row), axis=1)
    
    # Create a DataFrame to store the skewness values
    skewness_df = pd.DataFrame({'Skewness': skewness_values})
    
    # Plot the distribution of skewness values
    fig, ax = plt.subplots()
    skewness_df['Skewness'].plot(kind='hist', bins=30, ax=ax)
    ax.set_title('Distribution of Row Skewness')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')
    
    # Return the DataFrame and the Axes object
    return skewness_df, ax

# Example usage:
# data_matrix = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [5, 4, 3, 2, 1],
#     'C': [2, 3, 4, 5, 6]
# })
# skewness_df, ax = task_func(data_matrix)
# plt.show()
import unittest
import os
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
    def test_case_1(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        df, ax = task_func(data)
        self.verify_output(df, ax, data.shape[0], data)
    def test_case_2(self):
        data = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        df, ax = task_func(data)
        self.verify_output(df, ax, data.shape[0], data)
    def test_case_3(self):
        data = np.array([[3, 5, 7, 1000], [200, 5, 7, 1], [1, -9, 14, 700]])
        df, ax = task_func(data)
        self.verify_output(df, ax, data.shape[0], data)
    def test_case_4(self):
        data = np.array(
            [
                [1, 2, 3, 4, 5, 4, 3, 2, 1],
            ]
        )
        df, ax = task_func(data)
        self.verify_output(df, ax, data.shape[0], data)
    def test_case_5(self):
        data = np.array([[1, 1], [1, 1], [1, 1]])
        df, ax = task_func(data)
        # Check if DataFrame is returned with correct values
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 1))
        self.assertIn("Skewness", df.columns)
        # Check if Axes object is returned for the plot
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Distribution of Skewness")
    def verify_output(self, df, ax, expected_rows, data):
        # Check if DataFrame is returned with correct values
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (expected_rows, 1))
        self.assertIn("Skewness", df.columns)
        # Check if Axes object is returned for the plot
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Distribution of Skewness")
        # Check skewness values
        skewness = skew(data, axis=1)
        self.assertListEqual(df["Skewness"].tolist(), list(skewness))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)