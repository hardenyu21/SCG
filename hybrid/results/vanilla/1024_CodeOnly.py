import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
PLOT_TITLE = "Value Distribution"

def task_func(data_dict):
    # Create a DataFrame from the dictionary, excluding None values
    df = pd.DataFrame(data_dict).dropna()
    
    # Flatten the DataFrame to a single series for processing
    data_series = df.values.flatten()
    
    # Check if the DataFrame is empty or if all values are identical
    if data_series.size == 0 or np.all(data_series == data_series[0]):
        return df, None
    
    # Calculate the minimum and maximum values
    data_min = np.min(data_series)
    data_max = np.max(data_series)
    
    # Dynamically set the number of bins
    num_data_points = data_series.size
    num_bins = max(2, min(11, num_data_points // 2))
    
    # Create evenly spaced bin edges
    bin_edges = np.linspace(data_min, data_max, num_bins + 1)
    
    # Generate the histogram using seaborn
    plt.figure(figsize=(8, 6))
    ax = sns.histplot(data_series, bins=bin_edges, kde=False)
    
    # Set the plot title
    ax.set_title(PLOT_TITLE)
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# data_dict = {'A': [1, 2, 3, None, 5], 'B': [5, 4, 3, 2, 1]}
# df, ax = task_func(data_dict)
# if ax is not None:
#     plt.show()