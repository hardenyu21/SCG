from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace missing values with the column's average
    df_filled = df.fillna(df.mean())
    
    # Select numeric columns
    numeric_cols = df_filled.select_dtypes(include=['number']).columns
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    df_filled[numeric_cols] = scaler.fit_transform(df_filled[numeric_cols])
    
    # Calculate the correlation matrix
    corr_matrix = df_filled.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df_filled, ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, None, 5],
#     'B': [5, None, 1, 3, 2],
#     'C': [None, 1, 2, 3, 4]
# })
# standardized_df, heatmap_ax = task_func(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        df = pd.DataFrame(
            [[1, 2, 3], [4, 5, 6], [7, None, 9]], columns=["c1", "c2", "c3"]
        )
        # Expected output
        expected_df = df.copy()
        expected_df = expected_df.fillna(df.mean(axis=0))
        scaler = StandardScaler()
        expected_df[expected_df.columns] = scaler.fit_transform(
            expected_df[expected_df.columns]
        )
        # Function execution
        standardized_df, heatmap = task_func(df)
        pd.testing.assert_frame_equal(standardized_df, expected_df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)
        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)
    def test_case_2(self):
        df = pd.DataFrame([[3, 7, 9], [4, 1, 8], [2, 6, 5]], columns=["c1", "c2", "c3"])
        standardized_df, heatmap = task_func(df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)
        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)
    def test_case_3(self):
        df = pd.DataFrame([[4, 6, 8], [9, 5, 2], [3, 1, 7]], columns=["c1", "c2", "c3"])
        standardized_df, heatmap = task_func(df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)
        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)
    def test_case_4(self):
        df = pd.DataFrame([[9, 1, 2], [3, 4, 5], [7, 8, 6]], columns=["c1", "c2", "c3"])
        standardized_df, heatmap = task_func(df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)
        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)
    def test_case_5(self):
        df = pd.DataFrame(
            [[None, 17, 13], [None, None, 29], [42, 3, 100]], columns=["c1", "c2", "c3"]
        )
        standardized_df, heatmap = task_func(df)
        # Asserting the output DataFrame
        self.assertEqual(standardized_df.shape, df.shape)
        # Asserting the heatmap
        self.assertIsInstance(heatmap, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)