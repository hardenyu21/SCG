import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(range_start=0, range_end=10, step=0.1):
    def exp_generator():
        x = range_start
        while x <= range_end:
            yield (x, math.exp(x))
            x += step

    # Create the generator object
    gen = exp_generator()

    # Extract x and e^x values for plotting
    x_values = []
    exp_values = []
    for x, exp_x in gen:
        x_values.append(x)
        exp_values.append(exp_x)

    # Plot the exponential function
    fig, ax = plt.subplots()
    ax.plot(x_values, exp_values, label='e^x')
    ax.set_xlabel('x')
    ax.set_ylabel('e^x')
    ax.set_title('Exponential Function')
    ax.legend()

    # Show the plot
    plt.show()

    # Return the generator object and the Axes object
    return exp_generator(), ax

# Example usage
gen, ax = task_func()
import unittest
import doctest
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data, ax = task_func()
        # Check the first data point
        first_point = next(data)
        self.assertEqual(first_point, (0.0, 1.0))
        # Check plot title and labels
        self.assertEqual(ax.get_title(), "Exponential Function Plot")
        self.assertEqual(ax.get_xlabel(), "x")
        self.assertEqual(ax.get_ylabel(), "e^x")
        # Check if ax is an instance of Axes
        self.assertIsInstance(ax, Axes)
    # For brevity, similar test cases will be written for test_case_2 to test_case_5
    # These will test various attributes of the plotted data and generator object.
    def test_case_2(self):
        data, ax = task_func(11.4, 17.9, 0.2)
        self.assertIsInstance(ax, Axes)
        # Check the first data point
        first_point = next(data)
        self.assertEqual(first_point, (11.4, math.exp(11.4)))
    def test_case_3(self):
        data, ax = task_func(9.6, 15.2, 0.3)
        self.assertIsInstance(ax, Axes)
        # Check the last data point
        for point in data:
            pass
        self.assertAlmostEqual(point[0], 15.0, places=2)
        self.assertAlmostEqual(point[1], math.exp(15.0), places=2)
        
    def test_case_4(self):
        data, ax = task_func()
        self.assertIsInstance(ax, Axes)
        # Check the data in the axis object
        for point in data:
            ax.scatter(point[0], point[1], color='r')
        self.assertEqual(len(ax.get_children()), 210)
        
    def test_case_5(self):
        data, ax = task_func(89.0, 100.0, 0.1)
        self.assertIsInstance(ax, Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)