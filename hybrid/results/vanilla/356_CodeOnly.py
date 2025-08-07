import numpy as np
import matplotlib.pyplot as plt
import cmath

def task_func(x, y):
    # Check if x and y are numpy arrays
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("Both x and y must be numpy.ndarray.")
    
    # Check if x and y have the same length
    if x.shape != y.shape:
        raise ValueError("x and y must have the same shape.")
    
    # Create a meshgrid for x and y
    X, Y = np.meshgrid(x, y)
    
    # Calculate the complex function Z = X + iY
    Z = X + 1j * Y
    
    # Calculate the phase of the complex function
    phase = np.angle(Z)
    
    # Create a plot
    fig, ax = plt.subplots()
    c = ax.pcolormesh(X, Y, phase, cmap='hsv', shading='auto')
    ax.set_title('Phase of Complex Function')
    ax.set_xlabel('Real part (x)')
    ax.set_ylabel('Imaginary part (y)')
    fig.colorbar(c, ax=ax, label='Phase (radians)')
    
    # Return the axes object and the phase array
    return ax, phase

# Example usage:
# x = np.linspace(-1, 1, 100)
# y = np.linspace(-1, 1, 100)
# ax, phase = task_func(x, y)
# plt.show()