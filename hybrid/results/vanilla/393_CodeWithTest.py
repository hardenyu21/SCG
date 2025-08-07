import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, num_samples=1000, seed=77):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate samples from a normal distribution
    samples = np.random.normal(loc=mu, scale=sigma, size=num_samples)
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot the histogram
    axes[0].hist(samples, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    axes[0].set_title('Histogram')
    axes[0].set_xlabel('Value')
    axes[0].set_ylabel('Density')
    
    # Plot the Q-Q plot
    stats.probplot(samples, dist="norm", plot=axes[1])
    axes[1].set_title('Q-Q Plot')
    
    # Adjust layout
    plt.tight_layout()
    
    # Return the figure
    return fig

# Example usage:
# fig = task_func(mu=0, sigma=1)
# plt.show()
import unittest
from matplotlib import colors as mcolors
from matplotlib.figure import Figure
import doctest
class TestCases(unittest.TestCase):
    def test_standard_normal_distribution(self):
        """Test with standard normal distribution parameters (mu=0, sigma=1)."""
        fig = task_func(0, 1)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)  # Should contain two subplots
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def test_nonzero_mean(self):
        """Test with a nonzero mean."""
        mu = 5
        sigma = 1
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def test_different_standard_deviation(self):
        """Test with a different standard deviation."""
        mu = 0
        sigma = 2
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def test_negative_mean(self):
        """Test with a negative mean."""
        mu = -5
        sigma = 1
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def test_large_standard_deviation(self):
        """Test with a large standard deviation."""
        mu = 0
        sigma = 5
        fig = task_func(mu, sigma)
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 2)
        self._test_histogram_attributes(fig.axes[0], expected_bins=30, color='g')
        self._test_qq_plot_attributes(fig.axes[1])
    def _test_histogram_attributes(self, ax, expected_bins, color):
        """Helper function to test histogram attributes."""
        n, bins, patches = ax.hist([], bins=expected_bins, color=color)  # Dummy histogram to get attributes
        self.assertEqual(expected_bins, len(patches))  # The number of bars should match the number of bins
        self.assertEqual(patches[0].get_facecolor(), mcolors.to_rgba(color))  # Checking the color of the bars
    def _test_qq_plot_attributes(self, ax):
        """Helper function to test Q-Q plot attributes."""
        self.assertTrue(len(ax.get_lines()) > 0)  # Check if there are lines in the Q-Q plot


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)