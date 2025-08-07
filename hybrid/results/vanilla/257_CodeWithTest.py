import numpy as np
import matplotlib.pyplot as plt

def task_func(ax, num_turns):
    # Calculate the number of points for the spiral
    num_points = 1000
    theta = np.linspace(0, 2 * np.pi * num_turns, num_points)
    
    # Calculate the radius for each point
    r = theta
    
    # Plot the spiral
    ax.plot(theta, r, color='b')
    
    # Set the radial ticks
    radial_ticks = np.arange(0, num_turns * 45, 45)
    ax.set_rticks(radial_ticks)
    
    # Set the radial tick labels
    ax.set_rticklabels([f"{int(t)}°" for t in radial_ticks])
    
    # Set the title
    ax.set_title(f"Spiral with {num_turns} turns")
    
    # Return the modified Axes object
    return ax

# Example usage
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
task_func(ax, 3)
plt.show()
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.fig, self.ax = plt.subplots(subplot_kw={'polar': True})
    def test_positive_turns(self):
        """ Test the function with positive number of turns """
        num_turns = 3
        ax_modified = task_func(self.ax, num_turns)
        self.assertEqual(len(ax_modified.lines), 1)  # Checking if a spiral is plotted
        self.assertEqual(ax_modified.get_rlabel_position(), num_turns * 45)  # Radial label position
    def test_zero_turns(self):
        """ Test the function with zero turns """
        ax_modified = task_func(self.ax, 0)
        self.assertEqual(len(ax_modified.lines), 1)  # A line should still be plotted
    def test_negative_turns(self):
        """ Test the function with negative number of turns """
        ax_modified = task_func(self.ax, -3)
        self.assertEqual(len(ax_modified.lines), 1)  # A line should still be plotted
    def test_large_number_of_turns(self):
        """ Test the function with a large number of turns """
        ax_modified = task_func(self.ax, 100)
        self.assertEqual(len(ax_modified.lines), 1)  # A line should still be plotted
    def test_fractional_turns(self):
        """ Test the function with fractional number of turns """
        ax_modified = task_func(self.ax, 2.5)
        self.assertEqual(len(ax_modified.lines), 1)  # A line should still be plotted


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)