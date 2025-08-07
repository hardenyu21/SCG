from random import randint
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100):
    # Generate two arrays of random integers
    array1 = [randint(0, 100) for _ in range(array_length)]
    array2 = [randint(0, 100) for _ in range(array_length)]
    
    # Calculate the maximum values of the respective elements of the two arrays
    max_values = [max(a, b) for a, b in zip(array1, array2)]
    
    # Create a line diagram
    fig, ax = plt.subplots()
    ax.plot(max_values, label='Maximum Values')
    
    # Set the y-axis label
    ax.set_ylabel('Maximum Values')
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax

# Example usage
task_func()
import unittest
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        ax = task_func(50)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 50)
    def test_standard_functionality(self):
        """Test the function with default array length."""
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)
    def test_zero_length_array(self):
        """Test the function with zero array length."""
        ax = task_func(0)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 0)  # Expect no data points in the plot
    def test_non_default_length_array(self):
        """Test the function with non-default array lengths."""
        lengths = [50, 200]
        for length in lengths:
            ax = task_func(length)
            self.assertIsInstance(ax, plt.Axes)
            self.assertEqual(len(ax.lines[0].get_ydata()), length)
    def test_plot_output(self):
        """Verify the plot is generated and is of correct type."""
        ax = task_func()
        self.assertTrue(hasattr(ax, 'figure'), "Plot does not have associated figure attribute")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)