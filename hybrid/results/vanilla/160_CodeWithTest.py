import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    # Check if the input data has exactly eight columns
    if data.shape[1] != 8:
        raise ValueError("The input data must have exactly eight columns.")
    
    # Ensure the data is a DataFrame with the correct column names
    data.columns = COLUMN_NAMES
    
    # Compute the average of each row
    data['Average'] = data.mean(axis=1)
    
    # Plot the distribution of the averages
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(data['Average'], kde=True)
    ax.set_title('Distribution of Row Averages')
    ax.set_xlabel('Average')
    ax.set_ylabel('Frequency')
    
    # Evaluate normality using the normaltest
    p_value = None
    if len(data) >= 20:
        _, p_value = stats.normaltest(data['Average'])
    
    # Return the DataFrame, Axes object, and p-value
    return data, ax, p_value

# Example usage:
# df = pd.DataFrame(np.random.rand(100, 8))
# result_df, ax, p_value = task_func(df)
# plt.show()
# print("P-value:", p_value)
import numpy as np
import pandas as pd
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Mock plt.show to prevent it from displaying plots during tests
        self.addCleanup(plt.close, 'all')
    def test_basic_functionality(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax, p_value = task_func(data)
        expected_averages = [np.mean(row) for row in data]
        self.assertTrue(isinstance(df, pd.DataFrame), "Expected output to be a pandas DataFrame")
        self.assertIn('Average', df.columns, "DataFrame should have an 'Average' column")
        self.assertTrue(np.array_equal(df['Average'], expected_averages), "Averages are not calculated correctly")
        self.assertTrue(isinstance(ax, plt.Axes), "Expected a matplotlib Axes object for plotting")
    def test_empty_input(self):
        data = np.array([[]])
        with self.assertRaises(ValueError):
            task_func(data)
    def test_insufficient_columns(self):
        data = np.random.rand(10, 7)  # Only 7 columns, one less than required
        with self.assertRaises(ValueError):
            task_func(data)
    def test_non_numeric_input(self):
        data = np.array([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']])
        with self.assertRaises(TypeError):
            task_func(data)
    def test_plot_output(self):
        data = np.random.rand(20, 8)
        df, ax, _ = task_func(data)
        self.assertEqual(len(ax.lines), 1, "There should be one line on the plot")
    def test_normality_test(self):
        # Create a dataset large enough to properly trigger the normality test
        data = np.random.rand(20, 8)  # Increase to 20 rows
        df, ax, p_value = task_func(data)
        self.assertIsNotNone(p_value, "p-value should not be None for sufficient data size")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)