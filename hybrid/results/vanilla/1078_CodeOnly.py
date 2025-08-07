import numpy as np
import matplotlib.pyplot as plt

def task_func(arr):
    # Calculate the unique values and their counts
    unique, counts = np.unique(arr, return_counts=True)
    
    # Determine if the distribution is uniform
    uniform_distribution = np.all(counts == counts[0])
    
    # Create a histogram
    fig, ax = plt.subplots()
    ax.hist(arr, bins=np.arange(len(unique) + 1) - 0.5, edgecolor='black')
    
    # Set labels and title
    ax.set_xlabel('Unique Values')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Array Distribution')
    
    # Display the histogram
    plt.show()
    
    return uniform_distribution, ax

# Example usage:
# arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# uniform, ax = task_func(arr)
# print("Is the distribution uniform?", uniform)