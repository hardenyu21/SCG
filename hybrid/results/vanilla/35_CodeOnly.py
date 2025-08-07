import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, target_values=[1, 3, 4]):
    # Replace elements not in target_values with zeros
    for column in df.columns:
        df[column] = df[column].apply(lambda x: x if x in target_values else 0)
    
    # Create a figure and axes for plotting
    fig, axes = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(8, 4 * len(df.columns)))
    
    # Plot the distribution of each column
    for i, column in enumerate(df.columns):
        sns.countplot(data=df, x=column, ax=axes[i])
        axes[i].set_title(f'Distribution of {column}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Count')
    
    # Adjust layout
    plt.tight_layout()
    
    # Return the Axes object
    return axes

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [3, 4, 5, 6, 7],
#     'C': [1, 3, 4, 5, 6]
# })
# task_func(df)