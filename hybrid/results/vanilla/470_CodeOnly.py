import matplotlib.pyplot as plt
import numpy as np

def task_func(myList):
    # Determine the range of the data
    min_val = np.floor(min(myList))
    max_val = np.ceil(max(myList))
    
    # Create bin edges that align with integer values
    bins = np.arange(min_val, max_val + 1) - 0.5
    
    # Create the histogram
    fig, ax = plt.subplots()
    ax.hist(myList, bins=bins, edgecolor='black')
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    
    # Return the Axes object
    return ax