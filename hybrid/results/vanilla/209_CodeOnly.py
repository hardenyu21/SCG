import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Extract x and y values from the tuples
    x_values, y_values = zip(*data)
    
    # Find the tuple with the maximum value at index 1
    max_tuple = max(data, key=itemgetter(1))
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, label='Data Points')
    
    # Highlight the tuple with the maximum value at index 1
    ax.scatter(max_tuple[0], max_tuple[1], color='red', label='Max Tuple', zorder=5)
    
    # Set the title and labels
    ax.set_title('Max Tuple Highlighted')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax

# Example usage:
# data = [(1, 2), (3, 5), (5, 1), (2, 8)]
# task_func(data)