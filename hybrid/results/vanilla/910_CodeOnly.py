import numpy as np
import matplotlib.pyplot as plt

def task_func(letters, repetitions, colors):
    # Check if the input lists are empty
    if not letters or not colors:
        raise ValueError("The lists 'letters' and 'colors' cannot be empty.")
    
    # Check if the lengths of the input lists match
    if len(colors) != repetitions:
        raise ValueError("The length of the list 'colors' should match the number of repetitions of 'letters'.")
    
    # Flatten the list by repeating the original list
    flattened_list = letters * repetitions
    
    # Calculate the frequency of each letter
    unique_letters, counts = np.unique(flattened_list, return_counts=True)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    bar_container = ax.bar(unique_letters, counts, color=colors * (len(unique_letters) // len(colors) + 1))
    
    # Set the x-axis and y-axis labels and title
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Letters')
    
    # Return the Matplotlib Axes object
    return ax

# Example usage:
# letters = ['a', 'b', 'c']
# repetitions = 3
# colors = ['red', 'green', 'blue']
# ax = task_func(letters, repetitions, colors)
# plt.show()