import random
import string
import pandas as pd
import matplotlib.pyplot as plt

def task_func(n_rows=1000):
    if n_rows <= 0:
        raise ValueError("n_rows must be greater than 0.")
    
    # Generate random 3-letter strings
    random_strings = [''.join(random.choices(string.ascii_lowercase, k=3)) for _ in range(n_rows)]
    
    # Count the frequency of each string
    string_counts = pd.Series(random_strings).value_counts()
    
    # Get the top 30 most common strings
    top_30_strings = string_counts.head(30)
    
    # Plot the histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    top_30_strings.plot(kind='bar', ax=ax)
    ax.set_title('Top 30 Most Frequent 3-Letter Strings')
    ax.set_xlabel('3-Letter String')
    ax.set_ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return ax

# Example usage:
# ax = task_func(1000)
# plt.show()
import unittest
import random
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Tests for the function task_func."""
    def test_return_type(self):
        """Test if the function returns a Matplotlib Axes object."""
        random.seed(0)
        result = task_func(100)
        self.assertIsInstance(result, Axes)
    def test_default_parameter(self):
        """Test the function with the default parameter."""
        result = task_func()
        self.assertIsInstance(result, Axes)
    def test_zero_rows(self):
        """Test the function with zero rows."""
        with self.assertRaises(ValueError):
            task_func(0)
    def test_negative_rows(self):
        """Test the function with a negative number of rows."""
        with self.assertRaises(ValueError):
            task_func(-1)
    def test_large_number_of_rows(self):
        """Test the function with a large number of rows."""
        random.seed(2)
        result = task_func(10000)
        self.assertIsInstance(result, Axes)
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)