import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from random import sample

def task_func(df, tuples, n_plots):
    # Remove rows based on the list of tuples
    for row_values in tuples:
        df = df[~(df == list(row_values)).all(axis=1)]
    
    # Generate scatter plots for random combinations of two columns
    column_combinations = list(combinations(df.columns, 2))
    selected_combinations = sample(column_combinations, min(n_plots, len(column_combinations)))
    
    plots = []
    for col1, col2 in selected_combinations:
        fig, ax = plt.subplots()
        ax.scatter(df[col1], df[col2])
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        ax.set_title(f'Scatter plot of {col1} vs {col2}')
        plots.append(((col1, col2), fig))
    
    return df, plots