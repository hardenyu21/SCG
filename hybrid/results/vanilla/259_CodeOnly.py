import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def task_func(ax, num_points):
    # Check if ax is an instance of matplotlib.axes._axes.Axes
    if not isinstance(ax, matplotlib.axes._axes.Axes):
        raise ValueError("The input ax is not an Axes.")
    
    # Check if num_points is a non-negative integer
    if num_points < 0:
        raise ValueError("The number of points must be a non-negative integer.")
    
    # Generate random angles and radii
    angles = np.random.uniform(0, 2 * np.pi, num_points)
    radii = np.random.uniform(0, 1, num_points)
    
    # Plot the points on the polar plot
    ax.scatter(angles, radii)
    
    # Set the radial ticks based on the number of points divided by 10 degrees
    num_ticks = num_points // 10
    if num_ticks > 0:
        ax.set_rticks(np.linspace(0, 1, num_ticks + 1))
    
    return ax

# Example usage:
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# task_func(ax, 50)
# plt.show()