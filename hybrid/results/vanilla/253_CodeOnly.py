import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
COLORS = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def task_func(ax):
    # Generate random parameters for the sine wave
    amplitude = random.uniform(0.5, 1.5)
    frequency = random.uniform(1, 5)
    phase = random.uniform(0, 2 * np.pi)
    
    # Generate theta values
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the sine wave
    r = amplitude * np.sin(frequency * theta + phase)
    
    # Select a random color
    color = random.choice(COLORS)
    
    # Plot the sine wave on the polar subplot
    ax.plot(theta, r, color=color)
    
    # Set random positions for radial labels
    ax.set_rlabel_position(random.uniform(0, 360))
    
    # Return the color code of the plotted function
    return color

# Example usage
if __name__ == "__main__":
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    color = task_func(ax)
    print(f"Plotted color: {color}")
    plt.show()