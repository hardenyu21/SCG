import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, items=None, locations=None):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if 'Item' and 'Location' columns are present
    if 'Item' not in df.columns or 'Location' not in df.columns:
        raise ValueError("DataFrame must contain 'Item' and 'Location' columns.")
    
    # Define default lists if none are provided
    if items is None:
        items = ['Item1', 'Item2', 'Item3']  # Example default items
    if locations is None:
        locations = ['LocationA', 'LocationB', 'LocationC']  # Example default locations
    
    # Filter the DataFrame to include only specified items and locations
    filtered_df = df[df['Item'].isin(items) & df['Location'].isin(locations)]
    
    # Count the occurrences of each item per location
    item_location_counts = filtered_df.groupby(['Location', 'Item']).size().unstack(fill_value=0)
    
    # Plot the bar chart
    ax = item_location_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
    ax.set_title('Distribution of Items Across Locations')
    ax.set_xlabel('Location')
    ax.set_ylabel('Count')
    ax.legend(title='Item')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax
import unittest
import pandas as pd
import matplotlib.pyplot as plt
def get_bar_values(ax):
    """
    Extracts the heights of bars from a Matplotlib Axes object.
    Parameters:
    ax (Axes): A Matplotlib Axes object containing a bar chart.
    Returns:
    List[List[float]]: A list of lists containing the heights of the bars in each group.
    """
    values = []
    for container in ax.containers:
        values.append([bar.get_height() for bar in container])
    return values
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Item': ['apple', 'banana', 'apple', 'orange', 'grape', 'pineapple', 'banana', 'orange'],
            'Location': ['store1', 'store2', 'store1', 'store3', 'store4', 'store5', 'store3', 'store2']
        })
    def test_value(self):
        ax = task_func(self.df)
        self.assertIsInstance(ax, plt.Axes)
        bar_values = get_bar_values(ax)
            
        value = [[2.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0]]
        self.assertEqual(bar_values, value, "DataFrame contents should match the expected output")
        
    def test_return_type(self):
        ax = task_func(self.df)
        self.assertIsInstance(ax, plt.Axes)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}))
    def test_custom_items_and_locations(self):
        custom_items = ['item1', 'item2']
        custom_locations = ['loc1', 'loc2']
        df = pd.DataFrame({'Item': custom_items * 2, 'Location': custom_locations * 2})
        ax = task_func(df, items=custom_items, locations=custom_locations)
        self.assertIsInstance(ax, plt.Axes)
    def test_plot_title_and_labels(self):
        ax = task_func(self.df)
        self.assertEqual(ax.get_title(), 'Item Distribution by Location')
        self.assertEqual(ax.get_ylabel(), 'Count')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)