import numpy as np
import matplotlib.pyplot as plt

def task_func(ax, num_turns):
    # Calculate the number of points for the spiral
    num_points = 1000
    theta = np.linspace(0, 2 * np.pi * num_turns, num_points)
    
    # Calculate the radius for each point
    r = theta
    
    # Plot the spiral
    ax.plot(theta, r, color='b')
    
    # Set the radial ticks
    radial_ticks = np.arange(0, num_turns * 45, 45)
    ax.set_rticks(radial_ticks)
    
    # Set the radial tick labels
    ax.set_rticklabels([f"{int(t)}°" for t in radial_ticks])
    
    # Set the title
    ax.set_title(f"Spiral with {num_turns} turns")
    
    # Return the modified Axes object
    return ax

# Example usage
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
task_func(ax, 3)
plt.show()