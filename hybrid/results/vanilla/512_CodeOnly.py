import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check for negative values in the specified column
    if (data[column] < 0).any():
        raise ValueError("Quantity sold or total sales cannot be negative.")
    
    # Calculate sum, mean, min, and max of the column
    column_sum = data[column].sum()
    column_mean = data[column].mean()
    column_min = data[column].min()
    column_max = data[column].max()
    
    # Create a dictionary with the calculated statistics
    stats = {
        'sum': column_sum,
        'mean': column_mean,
        'min': column_min,
        'max': column_max
    }
    
    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(data['Product'], data[column])
    ax.set_title(f'Bar Chart of {column}')
    ax.set_xlabel('Product')
    ax.set_ylabel(column)
    
    # Return the statistics and the Axes object
    return stats, ax