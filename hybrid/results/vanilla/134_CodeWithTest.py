import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, bins=20):
    # Check if the input is a DataFrame and if it is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Get the name of the last column
    last_column_name = df.columns[-1]
    
    # Plot the histogram of the last column
    ax = df[last_column_name].plot(kind='hist', bins=bins, title=f'Histogram of {last_column_name}')
    
    # Set the labels for the axes
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax
import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        
    def test_return_type(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
    def test_invalid_input_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())
    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            task_func("not a dataframe")
    def test_histogram_bins(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        ax = task_func(df, bins=10)
        # plt.hist returns a tuple; to check the number of bins, we need to count the patches of the ax object
        self.assertEqual(len(ax.patches), 10)
    def test_plot_title_and_labels(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        ax = task_func(df)
        self.assertIn('Histogram of ', ax.get_title())
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
    def test_histogram_values(self):
        # Create a DataFrame with fixed values to ensure predictable histogram frequencies
        df = pd.DataFrame({'A': [1] * 10 + [2] * 20 + [3] * 30})
        ax = task_func(df, bins=3)  # Bins set to 3 to match the distinct values in 'A'
        n, bins, patches = ax.hist(df['A'], bins=3)
        # Expected frequencies: 10 for '1', 20 for '2', 30 for '3'
        expected_frequencies = [10, 20, 30]
        actual_frequencies = [p.get_height() for p in patches]
        self.assertEqual(actual_frequencies, expected_frequencies)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)