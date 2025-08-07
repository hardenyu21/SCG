from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace missing values with the column's average
    df_filled = df.fillna(df.mean())
    
    # Calculate Z-scores for numeric columns
    z_scores_df = df_filled.apply(zscore)
    
    # Initialize a list to store Axes objects
    axes_list = []
    
    # Plot histograms for each numeric column
    for column in z_scores_df.columns:
        fig, ax = plt.subplots()
        z_scores_df[column].hist(bins=10, ax=ax)
        ax.set_title(f'Histogram of Z-scores for {column}')
        ax.set_xlabel('Z-score')
        ax.set_ylabel('Frequency')
        axes_list.append(ax)
    
    # Return the DataFrame with Z-scores and the list of Axes objects
    return z_scores_df, axes_list