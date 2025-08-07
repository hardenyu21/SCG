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
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    def test_case_1(self):
        tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        modified_df, _ = task_func(self.df, tuples, 3)
        self.assertFalse(any(modified_df.apply(tuple, axis=1).isin(tuples)))
    def test_case_2(self):
        n_plots = 4
        _, plots = task_func(self.df, [], n_plots)
        self.assertEqual(len(plots), n_plots)
    def test_case_3(self):
        _, plots = task_func(self.df, [], 5)
        selected_columns = [plot[0] for plot in plots]
        self.assertTrue(len(selected_columns) == len(set(tuple(item) for item in selected_columns)))
    def test_case_4(self):
        modified_df, plots = task_func(self.df, [], 2)
        self.assertEqual(len(modified_df), len(self.df))
        self.assertEqual(len(plots), 2)
    def test_case_5(self):
        tuples = [(101, 202, 303, 404, 505), (606, 707, 808, 909, 1000)]
        modified_df, _ = task_func(self.df, tuples, 3)
        self.assertEqual(len(modified_df), len(self.df))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)