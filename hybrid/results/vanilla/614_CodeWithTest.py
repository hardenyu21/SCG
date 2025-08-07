import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(goals, penalties):
    # Create a DataFrame from the input data
    data = {
        'Team': list(goals.keys()),
        'Goals': list(goals.values()),
        'Penalties': list(penalties.values())
    }
    df = pd.DataFrame(data)
    
    # Create a pairplot using seaborn
    pairplot = sns.pairplot(df, vars=['Goals', 'Penalties'], hue='Team', diag_kind='kde')
    
    # Return the DataFrame and the Axes object
    return df, pairplot

# Example usage:
goals = {
    'Team A': 20,
    'Team B': 15,
    'Team C': 18,
    'Team D': 25
}

penalties = {
    'Team A': 5,
    'Team B': 3,
    'Team C': 4,
    'Team D': 6
}

df, pairplot = task_func(goals, penalties)
plt.show()
import unittest
from unittest.mock import patch
# Unit tests for the function task_func
class TestCases(unittest.TestCase):
    @patch('matplotlib.pyplot.show')
    def test_visualization_output(self, mock_show):
        goals = {'Team A': 3, 'Team B': 2, 'Team C': 0}
        penalties = {'Team A': 1, 'Team B': 0, 'Team C': 2}
        df, _ = task_func(goals, penalties)
        self.assertEqual(list(df.columns), ['Team', 'Goals', 'Penalties'])
        self.assertEqual(df['Goals'].sum(), 5)
        self.assertEqual(df['Penalties'].sum(), 3)
    def test_empty_input(self):
        goals = {}
        penalties = {}
        df, _ = task_func(goals, penalties)
        # The dataframe should have the teams but with 0 goals and penalties.
        expected_data = {
            'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
            'Goals': [0, 0, 0, 0, 0],
            'Penalties': [0, 0, 0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df)
    def test_plot_type(self):
        goals = {'Team A': 1}
        penalties = {'Team A': 1}
        _, plot = task_func(goals, penalties)
        self.assertIsInstance(plot, sns.axisgrid.PairGrid)
    def test_invalid_keys(self):
        goals = {'Team Z': 1}
        penalties = {'Team Z': 1}
        df, _ = task_func(goals, penalties)
        self.assertFalse('Team Z' in df['Team'].values)
    @patch('matplotlib.pyplot.show')
    def test_data_integrity(self, mock_show):
        goals = {'Team A': 3, 'Team B': 2, 'Team C': 1}
        penalties = {'Team A': 1, 'Team B': 2, 'Team C': 3}
        df, _ = task_func(goals, penalties)
        expected_data = {
            'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
            'Goals': [3, 2, 1, 0, 0],
            'Penalties': [1, 2, 3, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df, check_like=True)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)