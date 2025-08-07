import pandas as pd
import numpy as np

# Constants
COLUMNS = ['column1', 'column2', 'column3', 'column4', 'column5']

def task_func(df, dct):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame.")
    
    # Replace values in the DataFrame using the dictionary mapping
    df_replaced = df.replace(dct)
    
    # Calculate the Pearson correlation coefficient matrix
    correlation_matrix = df_replaced.corr(method='pearson')
    
    return correlation_matrix

# Example usage:
# df = pd.DataFrame({
#     'column1': [1, 2, 3, 4, 5],
#     'column2': [5, 4, 3, 2, 1],
#     'column3': [2, 3, 4, 5, 6],
#     'column4': [6, 5, 4, 3, 2],
#     'column5': [3, 4, 5, 6, 7]
# })
# dct = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# print(task_func(df, dct))