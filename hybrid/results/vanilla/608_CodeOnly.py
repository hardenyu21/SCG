import seaborn as sns
import pandas as pd
from random import sample
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    """
    Remove rows from a dataframe based on values of multiple columns, and then create n random pairs of two columns
    against each other to generate pairplots.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list of tuples): A list of tuples where each tuple contains a column name and a value to filter out.
    n_plots (int): The number of random pairplots to generate.

    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame after removing specified rows.
        list of Axes: A list containing the generated pairplots.
    """
    # Remove rows based on specified column-value pairs
    for col, value in tuples:
        df = df[df[col] != value]

    # Generate random pairs of columns for pairplots
    column_pairs = sample([(COLUMNS[i], COLUMNS[j]) for i in range(len(COLUMNS)) for j in range(i + 1, len(COLUMNS))], n_plots)

    # Create pairplots
    axes_list = []
    for col1, col2 in column_pairs:
        plt.figure()
        ax = sns.scatterplot(data=df, x=col1, y=col2)
        axes_list.append(ax)
        plt.title(f'Pairplot of {col1} vs {col2}')
        plt.show()

    return df, axes_list

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [5, 4, 3, 2, 1],
#     'C': [2, 3, 4, 5, 6],
#     'D': [6, 5, 4, 3, 2],
#     'E': [1, 1, 1, 1, 1]
# })
# modified_df, axes = task_func(df, [('A', 3), ('B', 2)], 3)