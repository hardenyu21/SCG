import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle

COLORS = ["b", "g", "r", "c", "m", "y", "k"]

def task_func(list_of_lists):
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Cycle through the colors
    color_cycle = cycle(COLORS)
    
    # Iterate over each list in the list_of_lists
    for y_values in list_of_lists:
        if not y_values:
            # Skip empty lists
            continue
        
        # Shuffle the y-values
        shuffled_y_values = y_values[:]
        shuffle(shuffled_y_values)
        
        # Create sequential x-values starting from 1
        x_values = np.arange(1, len(shuffled_y_values) + 1)
        
        # Get the next color from the cycle
        color = next(color_cycle)
        
        # Plot the line
        ax.plot(x_values, shuffled_y_values, color=color)
    
    # Show the plot
    plt.show()
    
    # Return the figure and axes objects
    return fig, ax