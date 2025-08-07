import pandas as pd
import numpy as np

def task_func(data, cols):
    # Convert the provided data into a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Calculate the correlation matrix of numeric columns
    correlation_matrix = df.corr()
    
    return correlation_matrix

# Example usage:
# data = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# cols = ['A', 'B', 'C']
# print(task_func(data, cols))