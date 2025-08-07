import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle

COLORS = ["b", "g", "r", "c", "m", "y", "k"]

def task_func(list_of_lists):
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Cycle through the colors
    color_cycle = cycle(COLORS)
    
    # Iterate over each list in the list_of_lists
    for y_values in list_of_lists:
        if not y_values:
            # Skip empty lists
            continue
        
        # Shuffle the y-values
        shuffled_y_values = y_values[:]
        shuffle(shuffled_y_values)
        
        # Create sequential x-values starting from 1
        x_values = np.arange(1, len(shuffled_y_values) + 1)
        
        # Get the next color from the cycle
        color = next(color_cycle)
        
        # Plot the line
        ax.plot(x_values, shuffled_y_values, color=color)
    
    # Show the plot
    plt.show()
    
    # Return the figure and axes objects
    return fig, ax
import unittest
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import matplotlib.colors as mcolors
import random
class TestCases(unittest.TestCase):
    """Tests for the function task_func."""
    def test_return_types(self):
        """Check that the function returns the correct types."""
        random.seed(0)
        fig, ax = task_func([["x", "y", "z"], ["a", "b", "c"]])
        self.assertIsInstance(
            fig,
            Figure,
            "The first return value should be an instance of matplotlib.figure.Figure.",
        )
        self.assertIsInstance(
            ax,
            Axes,
            "The second return value should be an instance of matplotlib.axes._axes.Axes.",
        )
    def test_number_of_lines(self):
        """Check that the correct number of lines are plotted."""
        random.seed(1)
        _, ax = task_func([["x", "y", "z"], ["a", "b", "c"]])
        self.assertEqual(
            len(ax.lines), 2, "There should be 2 lines plotted for 2 lists."
        )
        _, ax = task_func([["x", "y", "z"]])
        self.assertEqual(len(ax.lines), 1, "There should be 1 line plotted for 1 list.")
    def test_color_cycle(self):
        """Check that the colors of the plotted lines follow the specified cycle."""
        random.seed(2)
        _, ax = task_func([["x"], ["y"], ["z"], ["a"], ["b"], ["c"], ["d"], ["e"]])
        expected_colors = ["b", "g", "r", "c", "m", "y", "k", "b"]
        # Convert color codes to RGBA format
        expected_colors_rgba = [mcolors.to_rgba(c) for c in expected_colors]
        actual_colors_rgba = [line.get_color() for line in ax.lines]
        self.assertEqual(
            actual_colors_rgba,
            expected_colors_rgba,
            "The colors of the plotted lines should follow the specified cycle.",
        )
    def test_y_values(self):
        """Check that the y-values are shuffled."""
        random.seed(3)
        _, ax = task_func([["x", "y", "z"]])
        y_data = ax.lines[0].get_ydata()
        self.assertTrue(
            set(y_data) == {1, 2, 3},
            "The y-values should be shuffled numbers from the range [1, len(list)].",
        )
    def test_empty_input(self):
        """Check that no lines are plotted for an empty input list."""
        random.seed(4)
        _, ax = task_func([])
        self.assertEqual(
            len(ax.lines),
            0,
            "There should be no lines plotted for an empty input list.",
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)