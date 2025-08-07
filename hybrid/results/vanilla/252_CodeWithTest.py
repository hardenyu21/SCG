import matplotlib.pyplot as plt
from itertools import cycle, zip_longest

# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def task_func(data, labels):
    """
    Plots a list of data series with different colors. Cycles through predefined colors
    if there are more data series than colors. Uses 'black' for series beyond colors + labels.

    Parameters:
    data (list of lists): The data series to plot.
    labels (list of str): The labels for each data series.

    Returns:
    matplotlib.axes.Axes: The Axes object of the plot.
    """
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Cycle through colors and labels
    color_cycle = cycle(COLORS)
    label_cycle = cycle(labels)

    # Plot each data series
    for series, color, label in zip_longest(data, color_cycle, label_cycle, fillvalue='black'):
        ax.plot(series, label=label, color=color)

    # Add legend
    ax.legend()

    # Show plot
    plt.show()

    return ax

# Example usage:
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# labels = ['Series 1', 'Series 2', 'Series 3']
# task_func(data, labels)
import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
        labels = ['Series 1', 'Series 2', 'Series 3']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')
        self.assertEqual(lines[2].get_color(), 'blue')
    def test_case_2(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        labels = ['A', 'B', 'C', 'D']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[3].get_color(), 'yellow')
    def test_case_3(self):
        data = [[1, 2], [3, 4]]
        labels = ['X', 'Y']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')
    def test_case_4(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
        labels = ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5', 'Series 6']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[5].get_color(), 'black')
        
    def test_case_5(self):
        data = [[1, 2, 3], [4, 5, 6]]
        labels = []
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_color(), 'red')
        self.assertEqual(lines[1].get_color(), 'green')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)