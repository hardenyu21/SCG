import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col):
    # Check if the value column contains numeric data
    if not pd.api.types.is_numeric_dtype(df[value_col]):
        raise TypeError("The 'Value' column must contain numeric values.")
    
    # Group the data by the group column and calculate mean and standard deviation
    grouped = df.groupby(group_col)[value_col].agg(['mean', 'std']).reset_index()
    
    # Prepare data for plotting
    x = np.arange(len(grouped[group_col]))
    heights = grouped['mean']
    errors = grouped['std']
    
    # Create the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(x, heights, yerr=errors, capsize=5, color=[COLORS[i % len(COLORS)] for i in range(len(grouped))])
    
    # Set the title and labels
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    
    # Set the x-ticks to the group names
    ax.set_xticks(x)
    ax.set_xticklabels(grouped[group_col])
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax