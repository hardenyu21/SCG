from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def task_func(l, x_data, plot=False):
    # Define the quadratic function
    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

    # Fit the quadratic curve to the data
    params, _ = curve_fit(quadratic, x_data, l)

    # Calculate the fitted values
    fitted_values = quadratic(x_data, *params)

    # Plot the data and the fitted curve if plot=True
    ax = None
    if plot:
        fig, ax = plt.subplots()
        ax.scatter(x_data, l, label='Data', color='blue')
        ax.plot(x_data, fitted_values, label='Fitted Curve', color='red')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        plt.show()

    return params, fitted_values, ax

# Example usage:
# l = np.array([1, 4, 9, 16, 25])
# x_data = np.array([1, 2, 3, 4, 5])
# params, fitted_values, ax = task_func(l, x_data, plot=True)
# print("Parameters:", params)
# print("Fitted Values:", fitted_values)
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        l = np.array([1, 4, 9, 16, 25])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values = task_func(l, x_data)
        # Check the correctness of the fitted parameters
        self.assertAlmostEqual(params[0], 1.0, places=5)
        self.assertAlmostEqual(params[1], 0, places=5)
        # Check the correctness of the fitted values
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)
    def test_case_2(self):
        l = np.array([2, 5, 10, 17, 26])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values = task_func(l, x_data)
        # Check the correctness of the fitted values
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)
    def test_case_3(self):
        l = np.array([0, 3, 8, 15, 24])
        x_data = np.array([1, 2, 3, 4, 5])
        params, fitted_values, ax = task_func(l, x_data, plot=True)
        # Ensure the fitted values are correct
        np.testing.assert_array_almost_equal(fitted_values, l, decimal=5)
        # Ensure a plot is returned by checking the type of ax
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        x_data = np.array([1, 2, 3, 4, 5])
        l = x_data ** 2
        params, fitted_values, ax = task_func(l, x_data, plot=True)
        line = ax.lines[0].get_xydata()
        self.assertTrue(np.allclose(line[:, 1], l))  # The plotted curve should match the fitted values
    def test_case_5(self):
        x_data = np.array([1, 2, 3, 4, 5])
        l = x_data ** 2
        
        self.assertEqual(len(task_func(l, x_data, plot=False)), 2)  # If plot=False, no Axes object should be returned


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)