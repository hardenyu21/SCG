import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Constants
FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    # Check if the input is an Axes object
    if not isinstance(ax, matplotlib.axes._axes.Axes):
        raise ValueError("This function will raise a ValueError if the input ax is not an Axes.")
    
    # Select the function based on the index
    if func_index < 0 or func_index >= len(FUNCTIONS):
        raise IndexError("Function index is out of range.")
    
    func = FUNCTIONS[func_index]
    
    # Generate theta values from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Compute the radius using the selected function
    r = func(theta)
    
    # Plot the function on the polar plot
    ax.plot(theta, r)
    
    # Set radial ticks at positions corresponding to the index of the function multiplied by 45 degrees
    ax.set_rticks([func_index * 45 * np.pi / 180 for _ in range(5)])
    
    # Return the modified Axes object
    return ax

# Example usage
if __name__ == "__main__":
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    task_func(ax, 0)  # Plot sine function
    plt.show()