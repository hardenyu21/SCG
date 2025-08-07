import math
import numpy as np
import matplotlib.pyplot as plt

def task_func(list_input):
    # Sort the list based on the degree value of its elements
    sorted_list = sorted(list_input, key=lambda x: math.degrees(x))
    
    # Calculate the cumulative sum of the sorted list
    cumulative_sum = np.cumsum(sorted_list)
    
    # Plot the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumulative_sum, marker='o')
    ax.set_title('Cumulative Sum of Sorted List')
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    
    # Return the cumulative sum and the Axes object
    return cumulative_sum, ax

# Example usage:
# list_input = [math.radians(30), math.radians(60), math.radians(45)]
# cumulative_sum, ax = task_func(list_input)
# plt.show()