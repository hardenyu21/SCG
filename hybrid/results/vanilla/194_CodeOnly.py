import numpy as np
import matplotlib.pyplot as plt

# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

def task_func(data_size):
    # Generate random numeric data
    data = np.random.rand(data_size)
    
    # Randomly select a color for the histogram bars
    color = np.random.choice(BAR_COLOR)
    
    # Create a histogram of the data
    plt.hist(data, bins=10, color=color, edgecolor='black')
    plt.title('Histogram of Random Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the data and the color used
    return data, color

# Example usage
data, color = task_func(1000)
print(f"Data: {data}")
print(f"Color used for histogram: {color}")