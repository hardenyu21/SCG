import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    # Replace elements not in TARGET_VALUES with zeros
    df_transformed = df.applymap(lambda x: x if x in TARGET_VALUES else 0)
    
    # Initialize a figure for KDE plots
    fig, axes = plt.subplots(nrows=len(df_transformed.columns), ncols=1, figsize=(8, 4 * len(df_transformed.columns)))
    
    # Perform Box-Cox transformation on each column
    for i, column in enumerate(df_transformed.columns):
        data = df_transformed[column]
        
        # Check if data is constant
        if np.all(data == data[0]):
            # If constant, skip Box-Cox transformation
            transformed_data = data
        else:
            # Add 1 to data to handle zeros for Box-Cox transformation
            data_plus_one = data + 1
            transformed_data, _ = stats.boxcox(data_plus_one)
        
        # Plot KDE
        ax = axes[i] if len(df_transformed.columns) > 1 else axes
        ax.set_title(f'KDE of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Density')
        sns.kdeplot(transformed_data, ax=ax)
    
    # Adjust layout
    plt.tight_layout()
    
    return df_transformed, fig

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [3, 4, 5, 6, 7],
#     'C': [4, 5, 6, 7, 8]
# })
# transformed_df, fig = task_func(df)
# plt.show()
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        df = pd.DataFrame(
            {
                "A": [1, 2, 3, 4, 3, 2, 2, 1],
                "B": [7, 8, 9, 1, 2, 3, 5, 6],
                "C": [9, 7, 3, 1, 8, 6, 2, 1],
            }
        )
        transformed_df, fig = task_func(df)
        self.assertEqual(transformed_df.shape, df.shape)
    def test_case_2(self):
        df = pd.DataFrame({"A": [1, 1, 1], "B": [3, 3, 3], "C": [4, 4, 4]})
        transformed_df, fig = task_func(df)
        self.assertEqual(transformed_df.shape, df.shape)
        self.assertEqual(len(fig.axes[0].lines), 0)
        pd.testing.assert_frame_equal(transformed_df, df)
    def test_case_3(self):
        df = pd.DataFrame(
            {
                "A": [1, 7, 5, 4],
                "B": [3, 11, 1, 29],
                "C": [4, 9, 8, 4],
                "D": [16, 12, 20, 8],
            }
        )
        transformed_df, fig = task_func(df)
        self.assertEqual(transformed_df.shape, df.shape)
        self.assertEqual(len(fig.axes[0].lines), 3)
    def test_case_4(self):
        df = pd.DataFrame(
            {
                "E": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "F": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            }
        )
        transformed_df, fig = task_func(df)
        self.assertEqual(transformed_df.shape, df.shape)
        self.assertEqual(len(fig.axes[0].lines), 1)
    def test_case_5(self):
        df = pd.DataFrame(
            {
                "A": [0, 0, 0, 0],
            }
        )
        with self.assertRaises(ValueError):
            transformed_df, _ = task_func(df)
    def test_case_6(self):
        df = pd.DataFrame(
            {
                "A": [1, 2, 3, -4],
            }
        )
        with self.assertRaises(ValueError):
            transformed_df, _ = task_func(df)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)