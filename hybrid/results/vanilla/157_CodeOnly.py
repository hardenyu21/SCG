import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def task_func(data):
    # Check if the input is a 2D array
    if not isinstance(data, (list, np.ndarray)) or not all(isinstance(row, (list, np.ndarray)) for row in data):
        raise ValueError("Input data must be a 2D array.")
    
    # Convert the input data to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if all elements in the DataFrame are numeric
    if not np.issubdtype(df.values.dtype, np.number):
        raise ValueError("Input data must contain only numeric values.")
    
    # Calculate the average of each row and add it as a new column
    df['Average'] = df.mean(axis=1)
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Plot the heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df, ax

# Example usage:
# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# df, ax = task_func(data)