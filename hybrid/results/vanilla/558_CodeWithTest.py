import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(a, b, columns=['A', 'B']):
    # Combine the lists into a single 2D array
    data = np.array([a, b]).T
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    standardized_data = scaler.fit_transform(data)
    
    # Create a DataFrame with the standardized values
    df = pd.DataFrame(standardized_data, columns=columns)
    
    # Plot the standardized values using a bar plot
    ax = df.plot(kind='bar', figsize=(10, 6))
    ax.set_title('Standardized Values')
    ax.set_xlabel('Index')
    ax.set_ylabel('Standardized Value')
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# a = [1, 2, 3, 4, 5]
# b = [5, 4, 3, 2, 1]
# df, ax = task_func(a, b)
import unittest
import matplotlib
class TestCases(unittest.TestCase):
    def test_standard_case(self):
        """Test the function with non-empty lists."""
        df, ax = task_func([1, 2, 3], [4, 5, 6])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_empty_lists(self):
        """Test the function with empty lists."""
        df, ax = task_func([], [])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.empty, True)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_unequal_length_lists(self):
        """Test the function with lists of unequal length. Expecting an exception."""
        with self.assertRaises(ValueError):
            task_func([1, 2, 3], [4, 5])
    def test_single_value_lists(self):
        """Test the function with single-value lists."""
        df, ax = task_func([1], [1])
        self.assertEqual(df.shape, (1, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_large_lists(self):
        """Test the function with large lists."""
        df, ax = task_func(list(range(100)), list(range(100, 200)))
        self.assertEqual(df.shape, (100, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)