import pandas as pd
import matplotlib.pyplot as plt
from random import sample

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Remove rows from a dataframe based on column values and generate random scatter plots.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list): A list of tuples where each tuple contains a column name and a value.
                   Rows with these column-value pairs will be removed.
    n_plots (int): The number of random scatter plots to generate.

    Returns:
    pd.DataFrame: The DataFrame after removal of specified rows.
    list: A list containing matplotlib Axes objects of the generated plots.
    """
    # Remove rows based on specified column-value pairs
    for col, value in tuples:
        df = df[df[col] != value]

    # Generate random scatter plots
    axes = []
    for _ in range(n_plots):
        # Randomly select two columns for the scatter plot
        x_col, y_col = sample(COLUMNS, 2)
        
        # Create a scatter plot
        fig, ax = plt.subplots()
        ax.scatter(df[x_col], df[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f'Scatter plot of {x_col} vs {y_col}')
        
        # Append the Axes object to the list
        axes.append(ax)

    return df, axes