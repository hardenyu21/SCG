import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    # Check if the input is an Axes object
    if not isinstance(ax, matplotlib.axes._axes.Axes):
        raise ValueError("This function will raise a ValueError if the input ax is not an Axes.")
    
    # Select the function based on the index
    if func_index < 0 or func_index >= len(FUNCTIONS):
        raise IndexError("Function index is out of range.")
    
    func = FUNCTIONS[func_index]
    
    # Generate theta values from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Compute the radius using the selected function
    r = func(theta)
    
    # Plot the function on the polar plot
    ax.plot(theta, r)
    
    # Set radial ticks at positions corresponding to the index of the function multiplied by 45 degrees
    ax.set_rticks([func_index * 45 * np.pi / 180 for _ in range(5)])
    
    # Return the modified Axes object
    return ax

# Example usage
if __name__ == "__main__":
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    task_func(ax, 0)  # Plot sine function
    plt.show()
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, polar=True)
    def test_sine_function(self):
        ax = task_func(self.ax, 0)
        self.assertIsNotNone(ax, "Ax should not be None")
        # Verify if the plotted function matches the sine function
        x = np.linspace(0, 2 * np.pi, 1000)
        y_expected = np.sin(x)
        y_actual = ax.lines[0].get_ydata()
        np.testing.assert_allclose(y_actual, y_expected, atol=1e-5)
    def test_cosine_function(self):
        ax = task_func(self.ax, 1)
        self.assertIsNotNone(ax, "Ax should not be None")
    def test_tangent_function(self):
        ax = task_func(self.ax, 2)
        self.assertIsNotNone(ax, "Ax should not be None")
    def test_invalid_index(self):
        with self.assertRaises(IndexError):
            task_func(self.ax, 3)
    def test_rlabel_position(self):
        ax = task_func(self.ax, 1)
        self.assertEqual(ax.get_rlabel_position(), 45, "Rlabel position should be 45 for index 1")
    def test_case_non_ax(self):
        with self.assertRaises(ValueError):
            task_func("non_ax", 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)