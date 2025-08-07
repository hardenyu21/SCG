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