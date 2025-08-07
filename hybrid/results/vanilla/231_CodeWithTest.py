import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes

class ValueObject:
    value = 0
    def __init__(self, mu=0, std=1, seed=77):
        random.seed(seed)
        self.value = random.gauss(mu, std)

def task_func(obj_list) -> Axes:
    # Extract values from the list of ValueObjects
    values = [obj.value for obj in obj_list]
    
    # Calculate mean and standard deviation
    if values:
        mean = np.mean(values)
        std = np.std(values)
    else:
        mean = 0
        std = 0
    
    # Create a histogram of the values
    fig, ax = plt.subplots()
    ax.hist(values, bins=10, density=True, alpha=0.6, color='g', label='Histogram')
    
    # Plot the custom normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std)
    ax.plot(x, p, 'k', linewidth=2, label='Normal Distribution')
    
    # Add labels and legend
    ax.set_title('Histogram and Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Return the plotted Axes
    return ax

# Example usage:
# obj_list = [ValueObject(mu=5, std=2) for _ in range(100)]
# ax = task_func(obj_list)
# plt.show()
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with a small number of objects
        obj_list = [ValueObject(mu=23, std=77), ValueObject(mu=23, std=77, seed=222), ValueObject(mu=23, std=77, seed=333)]
        ax = task_func(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = 10.76,  std = 39.42")
    def test_case_2(self):
        # Testing with a larger number of objects
        obj_list = [ValueObject(mu=23, std=65) for _ in range(1000)]
        ax = task_func(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = 40.53,  std = 0.00")
    def test_case_3(self):
        # Testing with an even larger number of objects
        obj_list = [ValueObject(mu=23, std=77, seed=88), ValueObject(mu=11, std=99), ValueObject(mu=41, std=77)]
        ax = task_func(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = 27.52,  std = 32.92")
    def test_case_4(self):
        # Testing with an empty list of objects
        obj_list = []
        ax = task_func(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = 0.00,  std = 0.00")
    def test_case_5(self):
        # Testing with a single object
        obj_list = [ValueObject(mu=23, std=77, seed=12)]
        ax = task_func(obj_list)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Fit results: mu = -88.28,  std = 0.00")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)