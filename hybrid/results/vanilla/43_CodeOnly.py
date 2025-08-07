import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df):
    # Replace NaN values with the average of the column
    df_filled = df.apply(lambda col: col.fillna(col.mean()) if pd.api.types.is_numeric_dtype(col) else col)
    
    # Calculate statistics for each numeric column
    statistics = df_filled.describe()
    
    # Create a list to store the Axes objects
    axes_list = []
    
    # Plot distribution for each numeric column
    for column in df_filled.select_dtypes(include=[np.number]):
        plt.figure(figsize=(8, 6))
        ax = sns.histplot(df_filled[column], bins=10, kde=True)
        ax.set_title(f'Distribution of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        axes_list.append(ax)
    
    # Return the statistics DataFrame and the list of Axes objects
    return statistics, axes_list

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, np.nan, 4, 5],
#     'B': [5, np.nan, np.nan, 8, 10],
#     'C': ['x', 'y', 'z', 'w', 'v']
# })
# stats, axes = task_func(df)
# print(stats)
# for ax in axes:
#     plt.show()