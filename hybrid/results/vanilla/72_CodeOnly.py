import pandas as pd
import os
import numpy as np
import ast
import matplotlib.pyplot as plt

def task_func(directory):
    # Find the CSV file with the longest filename
    longest_filename = None
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            if longest_filename is None or len(filename) > len(longest_filename):
                longest_filename = filename
    
    # If no CSV file is found, return an empty DataFrame and None for the plot
    if longest_filename is None:
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None
    
    # Load the CSV file
    file_path = os.path.join(directory, longest_filename)
    df = pd.read_csv(file_path)
    
    # Convert the 'list' column from string representation to actual lists
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate sum, mean, and median for each list
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)
    
    # Plot the histogram of the median
    fig, ax = plt.subplots()
    if not df['median'].empty:
        ax.hist(df['median'], bins=10, edgecolor='black')
        ax.set_title('Histogram of Median Values')
        ax.set_xlabel('Median')
        ax.set_ylabel('Frequency')
    else:
        ax = None
    
    return df, ax