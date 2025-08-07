import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def task_func(a, b):
    # Calculate the Pearson correlation coefficient
    correlation_coefficient, _ = stats.pearsonr(a, b)
    
    # Create a Pandas DataFrame from the lists
    df = pd.DataFrame({'A': a, 'B': b})
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['A'], df['B'], label='Data points')
    
    # Calculate the regression line
    slope, intercept, _, _, _ = stats.linregress(df['A'], df['B'])
    regression_line = slope * df['A'] + intercept
    
    # Plot the regression line
    ax.plot(df['A'], regression_line, color='red', label='Regression line')
    
    # Add labels and legend
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.legend()
    
    # Return the correlation coefficient and the Axes object
    return correlation_coefficient, ax

# Example usage:
# a = [1, 2, 3, 4, 5]
# b = [2, 3, 5, 7, 11]
# corr_coeff, ax = task_func(a, b)
# plt.show()
import unittest
import math
import matplotlib
class TestCases(unittest.TestCase):
    def test_case_1(self):
        correlation, ax = task_func([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        self.assertAlmostEqual(correlation, 1.0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_2(self):
        correlation, ax = task_func([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
        self.assertTrue(math.isnan(correlation))
    def test_case_3(self):
        correlation, ax = task_func([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        self.assertAlmostEqual(correlation, -1.0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_4(self):
        correlation, ax = task_func([2, 4, 6, 8, 10], [1, 2, 3, 4, 5])
        self.assertAlmostEqual(correlation, 1.0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_5(self):
        correlation, ax = task_func([1, 3, 5, 7, 9], [9, 7, 5, 3, 1])
        self.assertAlmostEqual(correlation, -1.0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)