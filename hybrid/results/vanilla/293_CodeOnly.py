import itertools
import numpy as np
import matplotlib.pyplot as plt

def task_func(elements, subset_size):
    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Plot a histogram of the sums
    fig, ax = plt.subplots()
    ax.hist(subset_sums, bins='auto', alpha=0.7, color='blue', edgecolor='black')
    ax.set_title('Histogram of Subset Sums')
    ax.set_xlabel('Sum of Subset')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object, list of subsets, and list of subset sums
    return ax, subsets, subset_sums

# Example usage:
# elements = (1, 2, 3, 4)
# subset_size = 2
# ax, subsets, subset_sums = task_func(elements, subset_size)
# plt.show()