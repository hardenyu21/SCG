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