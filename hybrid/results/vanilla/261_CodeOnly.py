import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    # Check if the radius is negative
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    # Check if the provided Axes object is a polar plot
    if not ax.name == 'polar':
        raise TypeError("The provided Axes object is not a polar plot.")
    
    # Create an array of angles from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate the x and y coordinates for the circle
    r = np.full_like(theta, radius)
    
    # Plot the circle on the polar plot
    ax.plot(theta, r, label=f'Circle with radius {radius}')
    
    # Set radial ticks
    ax.set_rticks([radius / 2, radius, 3 * radius / 2])
    
    # Add a legend
    ax.legend(loc='upper right')
    
    # Return the modified Axes object
    return ax