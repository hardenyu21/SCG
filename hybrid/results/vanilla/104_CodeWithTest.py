import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

def task_func(df, groups=['A', 'B', 'C', 'D', 'E']):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if the required columns are present
    required_columns = ['date', 'value', 'group']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("DataFrame must contain 'date', 'value', and 'group' columns.")
    
    # Convert 'date' column to ordinal
    df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())
    
    # Create a color cycle for different groups
    colors = cycle(plt.cm.tab10.colors)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    for group in groups:
        group_data = df[df['group'] == group]
        if not group_data.empty:
            ax.scatter(group_data['date_ordinal'], group_data['value'], color=next(colors), label=group)
    
    # Set plot title and labels
    ax.set_title('Scatterplot of Values for Each Group Over Time')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.legend(title='Group')
    
    # Show the plot
    plt.show()
    
    return ax
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "group": ["A", "A", "A", "B", "B"],
            "date": pd.to_datetime(["2022-01-02", "2022-01-13", "2022-02-01", "2022-02-23", "2022-03-05"]),
            "value": [10, 20, 16, 31, 56],
        })
    def test_return_type(self):
        ax = task_func(self.df)
        self.assertIsInstance(ax, plt.Axes)
    def test_invalid_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}))
    def test_custom_groups(self):
        custom_groups = ['A', 'B']
        ax = task_func(self.df, groups=custom_groups)
        # Check if only the custom groups are plotted
        plotted_groups = set(self.df[self.df['group'].isin(custom_groups)]['group'].unique())
        self.assertEqual(len(plotted_groups), len(custom_groups))
    def test_plot_labels(self):
        ax = task_func(self.df)
        self.assertEqual(ax.get_xlabel(), 'Date (ordinal)')
        self.assertEqual(ax.get_ylabel(), 'Value')
        self.assertEqual(ax.get_title(), 'Scatterplot of Values for Each Group Over Time')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)