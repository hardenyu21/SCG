import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(dataframe):
    # Check if the DataFrame is empty
    if dataframe.empty:
        raise ValueError("The input DataFrame is empty.")
    
    # Check if the DataFrame has fewer than two columns
    if len(dataframe.columns) < 2:
        raise ValueError("The DataFrame must have at least two columns.")
    
    # Check if all columns are numeric
    if not all(np.issubdtype(dtype, np.number) for dtype in dataframe.dtypes):
        raise TypeError("All columns in the DataFrame must be numeric.")
    
    # Calculate the correlation matrix
    corr_matrix = dataframe.corr()
    
    # Find the pair of columns with the highest absolute correlation
    corr_matrix_abs = corr_matrix.abs()
    np.fill_diagonal(corr_matrix_abs.values, 0)  # Ignore self-correlation
    max_corr = corr_matrix_abs.max().max()
    max_corr_pair = corr_matrix_abs.stack().idxmax()
    
    # Unpack the pair of columns
    col1, col2 = max_corr_pair
    
    # Plot the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(dataframe[col1], dataframe[col2])
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.set_title(f'Scatter plot of {col1} vs {col2} (Correlation: {max_corr:.2f})')
    
    # Return the Axes object
    return ax