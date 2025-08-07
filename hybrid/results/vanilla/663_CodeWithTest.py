import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def task_func(x, y, labels):
    # Define the exponential function to fit
    def exp_func(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Create a figure and axis for plotting
    fig, ax = plt.subplots()

    # Fit the exponential curve to each set of data and plot
    for i in range(len(x)):
        # Fit the curve
        params, _ = curve_fit(exp_func, x[i], y[i])
        a, b, c = params

        # Generate x values for the fitted curve
        x_fit = np.linspace(min(x[i]), max(x[i]), 100)
        y_fit = exp_func(x_fit, a, b, c)

        # Plot the original data and the fitted curve
        ax.scatter(x[i], y[i], label=f'Data {labels[i]}', alpha=0.6)
        ax.plot(x_fit, y_fit, label=f'Fit {labels[i]}', linestyle='--')

    # Add labels and legend
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

    # Return the figure object
    return fig

# Example usage:
# x = [[1, 2, 3], [4, 5, 6]]
# y = [[2, 3, 5], [1, 2, 3]]
# labels = ['Set 1', 'Set 2']
# fig = task_func(x, y, labels)
# plt.show()
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Example data for all tests
        self.x = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([1, 3, 5])]
        self.y = [np.array([2, 3, 5]), np.array([5, 7, 10]), np.array([2.5, 3.5, 5.5])]
        self.labels = ["Test 1", "Test 2", "Test 3"]
    def test_plot_labels(self):
        """Ensure the plot includes all specified labels."""
        fig = task_func(self.x, self.y, self.labels)
        ax = fig.gca()
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertListEqual(legend_labels, self.labels, "Legend labels do not match input labels.")
    def test_curve_fit_success(self):
        """Verify that curve_fit successfully fits the data."""
        for x_arr, y_arr in zip(self.x, self.y):
            with self.subTest(x=x_arr, y=y_arr):
                popt, _ = curve_fit(lambda x, a, b, c: a * np.exp(-b * x) + c, x_arr, y_arr)
                self.assertTrue(len(popt) == 3, "Optimal parameters not found for the exponential fit.")
    def test_output_type(self):
        """Check the output type to be a matplotlib figure."""
        fig = task_func(self.x, self.y, self.labels)
        self.assertIsInstance(fig, plt.Figure, "Output is not a matplotlib figure.")
    def test_no_data(self):
        """Test the function with no data provided."""
        with self.assertRaises(ValueError, msg="Empty data lists should raise a ValueError."):
            task_func([], [], [])
    def test_non_numeric_data(self):
        """Ensure non-numeric data raises a ValueError during fitting."""
        x = [np.array(["a", "b", "c"])]
        y = [np.array(["d", "e", "f"])]
        labels = ["Invalid Data"]
        with self.assertRaises(ValueError, msg="Non-numeric data should raise a ValueError."):
            task_func(x, y, labels)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)