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