import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Histogram of samples')
    
    # Plot the normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2, label='Normal distribution')
    
    # Add labels and title
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Add legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the figure for testing purposes
    return fig
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        np.random.seed(42)
        mu = 0
        sigma = 1
        num_samples = 1000
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
    def test_case_2(self):
        np.random.seed(42)
        mu = 5
        sigma = 2
        num_samples = 1000
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
    def test_case_3(self):
        np.random.seed(42)
        mu = 0
        sigma = 1
        num_samples = 10
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
    def test_case_4(self):
        np.random.seed(42)
        mu = 0
        sigma = 1
        num_samples = 10
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)
    def test_case_5(self):
        np.random.seed(42)
        mu = 0
        sigma = 1
        num_samples = 10
        fig = task_func(mu, sigma, num_samples)
        ax = fig.gca()
        self.assertEqual(ax.get_title(), "Normal Distribution")
        self.assertTrue(len(ax.patches) > 0)
        self.assertTrue(len(ax.lines) > 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)