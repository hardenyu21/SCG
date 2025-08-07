import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_str, separator=",", bins=20):
    # Check if the input string is empty
    if not data_str.strip():
        raise ValueError("Data string is empty.")
    
    # Split the string into a list of values
    try:
        values = data_str.split(separator)
        # Convert the list of strings to a list of integers
        int_values = [int(value.strip()) for value in values]
    except ValueError:
        raise ValueError("Failed to convert data to integers.")
    
    # Create a pandas Series from the list of integers
    series = pd.Series(int_values, dtype='int64')
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(series, bins=bins, grid=True, rwidth=0.9, color='#607c8e')
    
    # Return the series and the Axes object
    return series, ax

# Example usage:
# series, ax = task_func("1,2,3,4,5,6,7,8,9,10")
# plt.show()