import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Extract x and y values from the data
    x_values, y_values = zip(*data)
    
    # Find the point with the maximum y-value
    max_y_point = max(data, key=itemgetter(1))
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, label='Data Points')
    
    # Highlight the point with the maximum y-value
    ax.scatter(max_y_point[0], max_y_point[1], color='red', zorder=5, label='Max Y Point')
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    
    # Return the axes object and the maximum y-value point
    return ax, max_y_point

# Example usage:
# data = [(1, 2), (2, 3), (3, 5), (4, 1)]
# ax, max_y_point = task_func(data)
# plt.show()
# print("Max Y Point:", max_y_point)