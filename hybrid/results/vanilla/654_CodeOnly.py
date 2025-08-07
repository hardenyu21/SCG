import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

def task_func(array, target_value):
    # Extract indices where the first column matches the target value
    indices = np.where(array[:, 0] == target_value)[0]
    
    # Define the exponential decay function
    def exp_decay(x, a, b, c):
        return a * np.exp(-b * x) + c
    
    # Initial guess for the parameters
    initial_guess = (1, 0.1, 0)
    
    # Perform the curve fitting
    popt, pcov = optimize.curve_fit(exp_decay, indices, array[indices, 1], p0=initial_guess)
    
    # Plot the data and the fitted curve
    fig, ax = plt.subplots()
    ax.scatter(indices, array[indices, 1], label='Data', color='blue')
    ax.plot(indices, exp_decay(indices, *popt), label='Fitted curve', color='red')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Exponential Decay Fit')
    ax.legend()
    
    # Return the optimized parameters and the Axes object
    return popt, ax

# Example usage:
# array = np.array([[1, 2.5], [1, 2.0], [1, 1.5], [2, 3.0], [2, 2.5]])
# target_value = 1
# popt, ax = task_func(array, target_value)
# plt.show()