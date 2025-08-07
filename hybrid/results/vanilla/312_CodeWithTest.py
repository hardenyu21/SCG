import random
import matplotlib.pyplot as plt
import numpy as np

# Constants
DISTRIBUTION_SIZE = 1000

def task_func(bins=30):
    # Generate a Gaussian distribution
    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=bins, density=True, alpha=0.75, color='blue')
    
    # Plot the Gaussian function for comparison
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = np.exp(-((x - 0) ** 2) / (2 * 1 ** 2)) / (1 * np.sqrt(2 * np.pi))
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set labels and title
    ax.set_title('Gaussian Distribution Histogram')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Show the plot
    plt.show()
    
    # Return the distribution and the Axes object
    return distribution, ax

# Example usage
distribution, ax = task_func()
import unittest
import matplotlib.pyplot as plt
import numpy as np
import random
class TestCases(unittest.TestCase):
    def test_histogram_axes_type(self):
        random.seed(0)
        _, ax = task_func()
        self.assertTrue(ax, plt.Axes)
        plt.close()
    def test_distribution_length(self):
        random.seed(0)
        distribution, _ = task_func()
        self.assertEqual(len(distribution), 1000)
        plt.close()
    def test_distribution_type(self):
        random.seed(0)
        distribution, _ = task_func()
        self.assertIsInstance(distribution, list, "Distribution should be a list")
        self.assertTrue(all(isinstance(x, float) for x in distribution))
        plt.close()
    def test_histogram_bin_count(self):
        random.seed(0)
        _, ax = task_func(bins=20)
        self.assertEqual(len(ax.patches), 20)
        plt.close()
    def test_default_bin_count(self):
        random.seed(0)
        _, ax = task_func()
        self.assertEqual(len(ax.patches), 30)
        plt.close()
    
    def test_plot_distribution(self):
        random.seed(0)
        distribution, ax = task_func()
        heights, bins, _ = plt.hist(distribution)
        expected_heights, _ = np.histogram(distribution, bins=bins)
        np.testing.assert_allclose(heights, expected_heights, rtol=0.1, err_msg="Distribution not plotted correctly")
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)