import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, bins=20):
    # Check if the input is a DataFrame and if it is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Get the name of the last column
    last_column_name = df.columns[-1]
    
    # Plot the histogram of the last column
    ax = df[last_column_name].plot(kind='hist', bins=bins, title=f'Histogram of {last_column_name}')
    
    # Set the labels for the axes
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax