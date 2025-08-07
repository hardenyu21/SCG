from random import randint
import matplotlib.pyplot as plt
import numpy as np

def task_func(array_length=100):
    # Generate two arrays of random integers
    array1 = [randint(0, 100) for _ in range(array_length)]
    array2 = [randint(0, 100) for _ in range(array_length)]
    
    # Calculate the maximum values of the respective elements of the two arrays
    max_values = [max(a, b) for a, b in zip(array1, array2)]
    
    # Create a line diagram
    fig, ax = plt.subplots()
    ax.plot(max_values, label='Maximum Values')
    
    # Set the y-axis label
    ax.set_ylabel('Maximum Values')
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax

# Example usage
task_func()