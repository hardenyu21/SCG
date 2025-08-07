import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def task_func(ax, num_points):
    # Check if ax is an instance of matplotlib.axes._axes.Axes
    if not isinstance(ax, matplotlib.axes._axes.Axes):
        raise ValueError("The input ax is not an Axes.")
    
    # Check if num_points is a non-negative integer
    if num_points < 0:
        raise ValueError("The number of points must be a non-negative integer.")
    
    # Generate random angles and radii
    angles = np.random.uniform(0, 2 * np.pi, num_points)
    radii = np.random.uniform(0, 1, num_points)
    
    # Plot the points on the polar plot
    ax.scatter(angles, radii)
    
    # Set the radial ticks based on the number of points divided by 10 degrees
    num_ticks = num_points // 10
    if num_ticks > 0:
        ax.set_rticks(np.linspace(0, 1, num_ticks + 1))
    
    return ax

# Example usage:
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# task_func(ax, 50)
# plt.show()
import unittest
import matplotlib.pyplot as plt
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with 10 points
        np.random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        modified_ax = task_func(ax, 10)
        self.assertIsInstance(modified_ax, plt.Axes, "Should return a matplotlib Axes object")
        self.assertEqual(modified_ax.get_rlabel_position(), 10 / 10, "Radial label position should be set to 1")
        plt.close()
    def test_case_2(self):
        # Test with 100 points
        np.random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        modified_ax = task_func(ax, 100)
        self.assertIsInstance(modified_ax, plt.Axes, "Should return a matplotlib Axes object")
        self.assertEqual(modified_ax.get_rlabel_position(), 100 / 10, "Radial label position should be set to 10")
        plt.close()
    def test_case_3(self):
        # Test with 50 points
        np.random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        modified_ax = task_func(ax, 50)
        self.assertIsInstance(modified_ax, plt.Axes, "Should return a matplotlib Axes object")
        self.assertEqual(modified_ax.get_rlabel_position(), 50 / 10, "Radial label position should be set to 5")
        plt.close()
    def test_case_4(self):
        # Test with 0 points (edge case)
        np.random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        modified_ax = task_func(ax, 0)
        self.assertIsInstance(modified_ax, plt.Axes, "Should return a matplotlib Axes object")
        self.assertEqual(modified_ax.get_rlabel_position(), 0 / 10, "Radial label position should be set to 0")
        plt.close()
    def test_case_5(self):
        # Test with negative points (invalid input)
        np.random.seed(0)
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        with self.assertRaises(ValueError, msg="Should raise ValueError for negative number of points"):
            task_func(ax, -10)
        plt.close()
    def test_case_6(self):
        with self.assertRaises(ValueError):
            task_func("non_ax", 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)