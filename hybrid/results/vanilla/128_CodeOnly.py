import numpy as np
import matplotlib.pyplot as plt
from random import randint

def task_func(POINTS=100):
    # Initialize arrays to store the x and y coordinates
    x_coords = np.zeros(POINTS)
    y_coords = np.zeros(POINTS)
    
    # Define possible directions: right, left, up, down
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Generate the random walk
    for i in range(1, POINTS):
        dx, dy = directions[randint(0, 3)]
        x_coords[i] = x_coords[i - 1] + dx
        y_coords[i] = y_coords[i - 1] + dy
    
    # Plot the random walk
    fig, ax = plt.subplots()
    ax.plot(x_coords, y_coords, marker='o', linestyle='-')
    ax.set_title('2D Random Walk')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.grid(True)
    
    # Show the plot
    plt.show()
    
    # Return the figure object
    return fig

# Example usage
task_func(100)