import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a non-empty DataFrame
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Select numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    # Check if there are any numeric columns
    if len(numeric_cols) == 0:
        raise ValueError("The DataFrame contains no numeric columns.")
    
    # Create a list to store the Axes objects
    axes_list = []
    
    # Plot histograms for each numeric column
    for col in numeric_cols:
        fig, ax = plt.subplots()
        df[col].hist(ax=ax)
        ax.set_title(col)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes_list.append(ax)
    
    return axes_list