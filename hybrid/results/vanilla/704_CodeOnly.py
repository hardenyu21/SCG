import pandas as pd
from itertools import combinations

# Constants
MIN_PERCENTAGE = 0.75

def task_func(data, cols, percentage=MIN_PERCENTAGE):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation
    between them is greater than a certain threshold.

    Parameters:
    - data (pd.DataFrame): The input DataFrame.
    - cols (list): A list of column names to consider for correlation.
    - percentage (float): The threshold for the absolute correlation value.

    Returns:
    - corr_combinations (list): A list of tuples where each tuple contains two column names.
    """
    corr_combinations = []

    # Calculate the correlation matrix for the specified columns
    corr_matrix = data[cols].corr().abs()

    # Iterate over all unique pairs of columns
    for col1, col2 in combinations(cols, 2):
        if corr_matrix.loc[col1, col2] > percentage:
            corr_combinations.append((col1, col2))

    return corr_combinations

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [5, 4, 3, 2, 1],
#     'C': [2, 3, 4, 5, 6],
#     'D': [6, 5, 4, 3, 2]
# })
# cols = ['A', 'B', 'C', 'D']
# result = task_func(df, cols)
# print(result)