import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    # Replace elements not in TARGET_VALUES with zeros
    df_transformed = df.applymap(lambda x: x if x in TARGET_VALUES else 0)
    
    # Initialize a figure for KDE plots
    fig, axes = plt.subplots(nrows=len(df_transformed.columns), ncols=1, figsize=(8, 4 * len(df_transformed.columns)))
    
    # Perform Box-Cox transformation on each column
    for i, column in enumerate(df_transformed.columns):
        data = df_transformed[column]
        
        # Check if data is constant
        if np.all(data == data[0]):
            # If constant, skip Box-Cox transformation
            transformed_data = data
        else:
            # Add 1 to data to handle zeros for Box-Cox transformation
            data_plus_one = data + 1
            transformed_data, _ = stats.boxcox(data_plus_one)
        
        # Plot KDE
        ax = axes[i] if len(df_transformed.columns) > 1 else axes
        ax.set_title(f'KDE of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Density')
        sns.kdeplot(transformed_data, ax=ax)
    
    # Adjust layout
    plt.tight_layout()
    
    return df_transformed, fig

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [3, 4, 5, 6, 7],
#     'C': [4, 5, 6, 7, 8]
# })
# transformed_df, fig = task_func(df)
# plt.show()