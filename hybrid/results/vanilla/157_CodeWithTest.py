import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def task_func(data):
    # Check if the input is a 2D array
    if not isinstance(data, (list, np.ndarray)) or not all(isinstance(row, (list, np.ndarray)) for row in data):
        raise ValueError("Input data must be a 2D array.")
    
    # Convert the input data to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if all elements in the DataFrame are numeric
    if not np.issubdtype(df.values.dtype, np.number):
        raise ValueError("Input data must contain only numeric values.")
    
    # Calculate the average of each row and add it as a new column
    df['Average'] = df.mean(axis=1)
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Plot the heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df, ax

# Example usage:
# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# df, ax = task_func(data)
import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a sample data set
        self.data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
    def tearDown(self):
        # Remove any files or handle other cleanup actions
        plt.close('all')
    def test_dataframe_structure(self):
        df, _ = task_func(self.data)
        self.assertIn('Average', df.columns, "DataFrame should contain an 'Average' column")
    def test_average_calculation(self):
        df, _ = task_func(self.data)
        expected_averages = [3.125, 3.375]  # The average of rows
        pd.testing.assert_series_equal(df['Average'], pd.Series(expected_averages, name='Average'), check_dtype=True)
    def test_heatmap_plot_returned(self):
        _, ax = task_func(self.data)
        self.assertIsInstance(ax, plt.Axes,
                              "The returned object should be a plt.Axes instance indicating a plot was created")
    def test_correlation_calculation(self):
        # Test to ensure that the correlation matrix is calculated correctly
        df, _ = task_func(self.data)
        expected_correlation = pd.DataFrame(self.data).corr()
        actual_correlation = \
            sns.heatmap(pd.DataFrame(self.data).corr(), annot=True, cmap='coolwarm').get_figure().axes[0].collections[
                0].get_array()
        np.testing.assert_array_almost_equal(actual_correlation, expected_correlation.to_numpy().ravel())
    def test_input_validation(self):
        # Test to ensure that non-2D arrays are handled properly
        with self.assertRaises(ValueError):
            task_func(np.array([1, 2, 3]))  # Not a 2D array


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)