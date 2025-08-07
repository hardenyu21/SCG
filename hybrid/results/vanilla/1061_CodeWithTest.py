import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculate the sum of elements in each row
    row_sums = np.sum(arr, axis=1)
    
    # Calculate the mean and standard deviation of the row sums
    mean = np.mean(row_sums)
    std = np.std(row_sums)
    
    # Normalize the row sums
    if std == 0:
        normalized_data = np.zeros_like(row_sums)
    else:
        normalized_data = (row_sums - mean) / std
    
    # Create a histogram of the normalized data
    fig, ax = plt.subplots()
    ax.hist(normalized_data, bins=30, density=True, alpha=0.6, color='green', label='Normalized Data')
    
    # Overlay the PDF of a standard normal distribution
    x = np.linspace(norm.ppf(0.005), norm.ppf(0.995), 100)
    ax.plot(x, norm.pdf(x), 'r-', lw=2, label='Standard Normal PDF')
    
    # Set the title and labels
    ax.set_title('Histogram of Normalized Data with Standard Normal PDF')
    ax.set_xlabel('Normalized Value')
    ax.set_ylabel('Probability Density')
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax, normalized_data
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    """Tests for `task_func`."""
    def test_histogram_and_pdf(self):
        """Test that the histogram and PDF are plotted."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        ax, _ = task_func(arr)
        self.assertEqual(
            ax.get_title(),
            "Histogram of Normalized Data with Standard Normal PDF",
        )
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(len(ax.patches), 30)
    def test_normalized_data(self):
        """Test that the normalized data is correct."""
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        _, normalized_data = task_func(arr)
        expected_data = [-1.22474487, 0.0, 1.22474487]
        for i in range(len(expected_data)):
            self.assertTrue(np.isclose(normalized_data[i], expected_data[i]))
    def test_empty_array(self):
        """Test empty array."""
        arr = np.array([[], [], []])
        _, normalized_data = task_func(arr)
        for value in normalized_data:
            self.assertTrue(np.isclose(value, 0))
    def test_single_value_array(self):
        """Test single value array."""
        arr = np.array([[5], [5], [5]])
        _, normalized_data = task_func(arr)
        for value in normalized_data:
            self.assertTrue(np.isclose(value, 0))
    def test_large_values(self):
        """Test large values."""
        arr = np.array([[1e6, 2e6, 3e6], [4e6, 5e6, 6e6], [7e6, 8e6, 9e6]])
        _, normalized_data = task_func(arr)
        expected_data = [-1.22474487, 0.0, 1.22474487]
        for i in range(len(expected_data)):
            self.assertTrue(np.isclose(normalized_data[i], expected_data[i]))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)