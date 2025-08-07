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
import unittest
from unittest.mock import patch
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=COLUMNS)
        self.tuples = [(self.df.iloc[0].values), (self.df.iloc[1].values)]
    def test_no_plots_generated(self):
        """Test case with zero plots requested."""
        _, plots = task_func(self.df, [], 0)  # Request 0 plots.
        self.assertEqual(len(plots), 0, "No plots should be generated when n_plots is 0.")
    def test_plot_generation(self):
        _, plots = task_func(self.df, [], 3)
        self.assertEqual(len(plots), 3, "Should generate exactly 3 plots.")
    @patch('matplotlib.pyplot.show')
    def test_empty_dataframe(self, mock_show):
        empty_df = pd.DataFrame(columns=COLUMNS)
        modified_df, plots = task_func(empty_df, [], 2)
        self.assertTrue(modified_df.empty, "DataFrame should be empty.")
        self.assertEqual(len(plots), 2, "Should attempt to generate 2 plots even for an empty DataFrame.")
    def test_no_row_removal(self):
        modified_df, _ = task_func(self.df, [(999, 999, 999, 999, 999)], 0)
        self.assertEqual(len(modified_df), len(self.df), "No rows should be removed.")
    def test_random_plot_columns(self):
        _, plots = task_func(self.df, [], 1)
        # Assuming task_func generates at least one plot and adds it to the list,
        # access the first plot for testing.
        first_plot = plots[0]
        plot_columns = [first_plot.get_xlabel(), first_plot.get_ylabel()]
        self.assertIn(plot_columns[0], COLUMNS, "X-axis should be from COLUMNS.")
        self.assertIn(plot_columns[1], COLUMNS, "Y-axis should be from COLUMNS.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)