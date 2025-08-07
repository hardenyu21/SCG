import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(data_list):
    # Check if the data_list is empty
    if not data_list:
        raise ValueError("The data_list is empty.")
    
    # Unzip the list of tuples
    unzipped_data = list(itertools.zip_longest(*data_list))
    
    # Plot the numerical values for each position
    fig, ax = plt.subplots()
    for i, data in enumerate(unzipped_data):
        ax.plot(data, label=f'Position {i}')
    
    # Add labels and legend
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax