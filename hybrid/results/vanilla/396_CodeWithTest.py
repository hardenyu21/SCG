import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, sample_size, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a random sample from a normal distribution
    sample = np.random.normal(loc=mu, scale=sigma, size=sample_size)
    
    # Create a Gaussian kernel density estimate
    kde = stats.gaussian_kde(sample)
    
    # Define the range for the x-axis
    x = np.linspace(min(sample), max(sample), 1000)
    
    # Plot the KDE
    fig, ax = plt.subplots()
    ax.plot(x, kde(x), label='KDE')
    
    # Plot the original normal distribution for comparison
    ax.plot(x, stats.norm.pdf(x, mu, sigma), label='True Distribution', linestyle='--')
    
    # Add labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func(mu=0, sigma=1, sample_size=1000)
# plt.show()
import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        with self.assertRaises(ValueError):
            ax = task_func(0, 1, 0, 77)        
    def test_case_2(self):
        mu, sigma, sample_size, seed = 0, 1, 10000, 42
        ax = task_func(mu, sigma, sample_size, seed)
        line = ax.lines[0]
        x_data, y_data = line.get_data()
        assert isinstance(ax, matplotlib.axes._axes.Axes)
        assert min(x_data) < mu - 3*sigma and max(x_data) > mu + 3*sigma
    def test_case_3(self):
        ax = task_func(0, 1, 10000, 42)
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        assert xlim[0] < 0 and xlim[1] > 0
        assert ylim[0] < 0 and ylim[1] > 0
    def test_case_4(self):
        ax = task_func(0, 1, 1000, 42)
        assert len(ax.lines) == 1
    def test_case_5(self):
        ax1 = task_func(0, 1, 42)
        ax2 = task_func(0, 1, 42)
        line1 = ax1.lines[0]
        line2 = ax2.lines[0]
        x_data1, y_data1 = line1.get_data()
        x_data2, y_data2 = line2.get_data()
        assert np.array_equal(x_data1, x_data2) and np.array_equal(y_data1, y_data2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)