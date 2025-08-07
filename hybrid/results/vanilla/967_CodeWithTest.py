import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def task_func(func, x_range=(-2, 2), num_points=1000):
    # Generate linearly spaced x-values
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    
    # Calculate the function values
    y_values = func(x_values)
    
    # Calculate the cumulative integral of the function
    cumulative_integral = integrate.cumtrapz(y_values, x_values, initial=0)
    
    # Create the plot
    fig, ax = plt.subplots()
    
    # Plot the function
    ax.plot(x_values, y_values, label=f'{func.__name__}(x)')
    
    # Plot the cumulative integral
    ax.plot(x_values, cumulative_integral, label=f'Integral of {func.__name__}(x)')
    
    # Add legend and labels
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Plot of {func.__name__}(x) and its Integral')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax

# Example usage:
# Define a sample function
def sample_function(x):
    return np.sin(x)

# Call the task_func with the sample function
task_func(sample_function)
import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    def tearDown(self):
        plt.close("all")
    def helper_assert_plot_attributes(self, func):
        # Test plot attributes are as expected
        ax = task_func(func)
        function_name = func.__name__
        legend_labels = ax.get_legend_handles_labels()[-1]
        self.assertIsInstance(ax, Axes)
        self.assertIn(function_name, legend_labels[0])
        self.assertIn(function_name, legend_labels[1])
    def test_case_1(self):
        # Test basic case in docstring
        ax = task_func(np.sin)
        self.helper_assert_plot_attributes(np.sin)
    def test_case_2(self):
        # Test other functions - numpy
        for func in [np.cos, np.exp]:
            ax = task_func(func)
            self.helper_assert_plot_attributes(func)
    def test_case_3(self):
        # Test other functions - lambda
        func = lambda x: x ** 2
        ax = task_func(func)
        self.helper_assert_plot_attributes(func)
    def test_case_4(self):
        # Test custom range and points
        ax = task_func(np.cos, x_range=(0, np.pi), num_points=500)
        self.assertEqual(len(ax.lines[0].get_xdata()), 500)
        self.assertEqual(ax.lines[0].get_xdata()[0], 0)
        self.assertEqual(ax.lines[0].get_xdata()[-1], np.pi)
    def test_case_5(self):
        # Test correct integral calculation
        # Test integral of x^2 in the range [0,1], should be close to 1/3
        func = lambda x: x ** 2
        X = np.linspace(0, 1, 1000)
        expected_integral = 1 / 3 * X ** 3  # Analytical integral of x^2
        ax = task_func(func, x_range=(0, 1), num_points=1000)
        computed_integral = ax.lines[1].get_ydata()[
            -1
        ]  # Last value of the computed integral
        self.assertAlmostEqual(computed_integral, expected_integral[-1], places=4)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)