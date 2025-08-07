import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

def task_func(X, Y):
    # Fit the quadratic function to the data
    params, covariance = curve_fit(quadratic_function, X, Y)
    
    # Extract the optimized parameters
    a, b, c = params
    
    # Generate x values for the plot
    x_fit = np.linspace(min(X), max(X), 100)
    # Calculate the fitted y values
    y_fit = quadratic_function(x_fit, a, b, c)
    
    # Plot the data and the fit
    fig, ax = plt.subplots()
    ax.scatter(X, Y, label='Data', color='blue')
    ax.plot(x_fit, y_fit, label='Quadratic Fit', color='red')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.set_title('Quadratic Fit to Data')
    
    # Return the optimized parameters and the plot
    return (a, b, c), ax

# Example usage:
# X = np.array([1, 2, 3, 4, 5])
# Y = np.array([2, 4, 6, 8, 10])
# params, ax = task_func(X, Y)
# plt.show()