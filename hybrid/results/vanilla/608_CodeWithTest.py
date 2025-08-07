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
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Common setup for generating DataFrame for testing
        self.df = pd.DataFrame({
            'A': list(range(0, 100, 10)) + [10, 60],
            'B': list(range(10, 110, 10)) + [20, 70],
            'C': list(range(20, 120, 10)) + [30, 80],
            'D': list(range(30, 130, 10)) + [40, 90],
            'E': list(range(40, 140, 10)) + [50, 100]
        })
    def test_case_1(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, plots = task_func(self.df, tuples, 3)
        self.assertTrue(all(tuple(row) not in tuples for row in modified_df.to_numpy()))
        # Check the number of plots does not exceed min(n_plots, len(df.columns) // 2)
        expected_plot_count = min(3, len(self.df.columns) // 2)
        self.assertEqual(len(plots), expected_plot_count)
    def test_case_2(self):
        tuples = [(200, 200, 200, 200, 200), (300, 300, 300, 300, 300)]
        modified_df, plots = task_func(self.df, tuples, 2)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 2)
    def test_case_3(self):
        tuples = []
        modified_df, plots = task_func(self.df, tuples, 1)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 1)
    def test_case_4(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, plots = task_func(self.df, tuples, 0)
        self.assertTrue(all(row not in modified_df.values for row in tuples))
        self.assertEqual(len(plots), 0)
    def test_case_5(self):
        tuples = [(10, 20, 30, 40, 50), (200, 200, 200, 200, 200)]
        modified_df, plots = task_func(self.df, tuples, 4)
        # Ensure the specific tuple is not in the DataFrame
        self.assertTrue((10, 20, 30, 40, 50) not in modified_df.values)
        # Check the number of plots does not exceed min(n_plots, len(df.columns) // 2)
        expected_plot_count = min(4, len(self.df.columns) // 2)
        self.assertEqual(len(plots), expected_plot_count)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)