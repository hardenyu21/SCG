import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_groups=5, data_size=5, labels=None):
    # Generate random data
    np.random.seed(0)  # For reproducibility
    data = np.random.randint(1, 100, size=(data_size, num_groups))
    
    # Create a DataFrame
    if labels is None:
        labels = [f'Category {i+1}' for i in range(num_groups)]
    df = pd.DataFrame(data, columns=labels)
    
    # Plotting
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Stacked Bar Chart of Random Data')
    ax.set_xlabel('Data Points')
    ax.set_ylabel('Values')
    ax.legend(title='Categories')
    
    # Save the plot to a file
    filename = 'test_plot.png'
    plt.savefig(filename)
    
    # Return the Figure object, DataFrame, and filename
    return fig, df, filename

# Example usage
fig, df, filename = task_func()
print(f"DataFrame:\n{df}")
print(f"Plot saved to: {filename}")
import unittest
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')
class TestCases(unittest.TestCase):
    def tearDown(self):
        """Ensure no files are left after tests."""
        try:
            os.remove('test_plot.png')
        except FileNotFoundError:
            pass
    def test_default_parameters(self):
        """Test the function with default parameters."""
        fig, data, plot_filename = task_func()
        self.assertIsInstance(fig, plt.Figure, "The function should return a matplotlib.figure.Figure object.")
        self.assertEqual(data.shape, (5, 5), "The default DataFrame should have 5 rows and 5 columns.")
        expected_columns = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
        self.assertListEqual(list(data.columns), expected_columns, "Default column labels are incorrect.")
        self.assertTrue(os.path.exists(plot_filename), "Plot file should be created.")
    def test_custom_parameters(self):
        """Test the function with custom number of groups, data size, and labels."""
        num_groups, data_size, labels = 3, 4, ['A', 'B', 'C']
        fig, data, plot_filename = task_func(num_groups=num_groups, data_size=data_size, labels=labels)
        self.assertIsInstance(fig, plt.Figure, "The function should return a matplotlib.figure.Figure object.")
        self.assertEqual(data.shape, (4, 3), "DataFrame dimensions should match the custom parameters.")
        self.assertListEqual(list(data.columns), labels, "Column labels should match the custom labels provided.")
    def test_data_values(self):
        """Test that the data in the DataFrame is within the expected range (0.0, 1.0)."""
        fig, data, plot_filename = task_func()
        self.assertTrue((data >= 0.0).all().all() and (data <= 1.0).all().all(),
                        "All data should be within the range [0.0, 1.0].")
    def test_no_labels_provided(self):
        """Test that default labels are used when no labels are provided."""
        fig, data, plot_filename = task_func(num_groups=3)
        expected_columns = ['Group1', 'Group2', 'Group3']
        self.assertListEqual(list(data.columns), expected_columns,
                             "Default column labels are incorrect when no labels are provided.")
    def test_plot_file_cleanup(self):
        """Test that the plot file is cleaned up after a test."""
        fig, data, plot_filename = task_func()
        self.assertTrue(os.path.exists(plot_filename), "Plot file should exist immediately after creation.")
        os.remove(plot_filename)
        self.assertFalse(os.path.exists(plot_filename), "Plot file should be deleted in tearDown.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)