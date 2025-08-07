import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from itertools import chain

def task_func(L):
    # Flatten the list of lists
    flattened_list = list(chain.from_iterable(L))
    
    # Convert to a numpy array of integers
    data = np.array(flattened_list, dtype=int)
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(data)
    
    # Plot the histogram
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Plot the normal distribution overlay
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Add labels and title
    ax.set_title('Histogram with Normal Distribution Overlay')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Show the plot
    plt.show()
    
    return ax
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ax = task_func(L)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        L = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        ax = task_func(L)
        self.assertIsInstance(ax, plt.Axes)
        # self.assertIn("Fit results:", ax.get_title())
    def test_case_3(self):
        L = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        ax = task_func(L)
        self.assertIsInstance(ax, plt.Axes)
        # self.assertIn("Fit results:", ax.get_title())
    def test_case_4(self):
        L = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ax = task_func(L)
        self.assertIsInstance(ax, plt.Axes)
        # self.assertIn("Fit results:", ax.get_title())
    def test_case_5(self):
        L = [[5, 15, 25], [35, 45, 55], [65, 75, 85]]
        ax = task_func(L)
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)