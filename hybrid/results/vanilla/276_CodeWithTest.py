import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(matrix):
    # Calculate the maximum value of each row
    max_values = np.max(matrix, axis=1)
    
    # Calculate the histogram of the maximum values
    counts, bin_edges = np.histogram(max_values, bins='auto', density=True)
    
    # Estimate the core density of the distribution using a Gaussian kernel
    kernel_density = stats.gaussian_kde(max_values)
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(max_values, bins=bin_edges, alpha=0.6, color='g', density=True, label='Histogram')
    
    # Plot the kernel density estimate
    x = np.linspace(min(max_values), max(max_values), 1000)
    ax.plot(x, kernel_density(x), 'r-', label='Kernel Density Estimate')
    
    # Add labels and legend
    ax.set_title('Distribution of Maximum Values')
    ax.set_xlabel('Maximum Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Return the skewness, kurtosis, and the histogram plot
    return skewness, kurtosis, ax

# Example usage:
# matrix = np.random.rand(100, 5)  # Example matrix
# skewness, kurtosis, ax = task_func(matrix)
# plt.show()
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a small matrix
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        skew, kurtosis, ax = task_func(matrix)
        
        self.assertEqual(skew, 0.0)
        self.assertEqual(kurtosis, -1.5)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        # Test with negative values
        matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        skew, kurtosis, ax = task_func(matrix)
        
        self.assertEqual(skew, 0.0)
        self.assertEqual(kurtosis, -1.5)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_3(self):
        # Test with larger numbers
        matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
        skew, kurtosis, ax = task_func(matrix)
        
        self.assertEqual(skew, 0.0)
        self.assertEqual(kurtosis, -1.5)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        # Test with identical rows
        matrix = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        skew, kurtosis, ax = task_func(matrix)
        
        self.assertFalse(np.isnan(skew))
        self.assertFalse(np.isnan(kurtosis))
        self.assertIsInstance(ax, plt.Axes)
    def test_case_5(self):
        # Test with a single row
        matrix = [[1, 2, 3]]
        skew, kurtosis, ax = task_func(matrix)
        
        self.assertFalse(np.isnan(skew))  # Skew is defined
        self.assertFalse(np.isnan(kurtosis))  # Kurtosis is defined
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)