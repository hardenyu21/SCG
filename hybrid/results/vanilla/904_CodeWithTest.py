import pandas as pd
import matplotlib.pyplot as plt

def task_func(d, keys=['x', 'y', 'z']):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)
    
    # Check if the specified keys exist in the DataFrame
    for key in keys:
        if key not in df.columns:
            raise ValueError(f"Key '{key}' not found in the data.")
    
    # Plot the specified keys
    ax = df.plot(x=keys[0], y=keys[1:], kind='line', marker='o')
    
    # Set labels and title
    ax.set_xlabel(keys[0])
    ax.set_ylabel('Values')
    ax.set_title('Plot of specified keys')
    
    # Return the Matplotlib Axes object
    return ax
import unittest
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    
    def test_basic_input(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        ax = task_func(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(set([text.get_text() for text in ax.legend_.texts]), {'x', 'y', 'z'})
        self.assertEqual(len(ax.lines), 3)
    def test_missing_keys_in_data(self):
        data = [{'x': 1, 'y': 10}, {'y': 15, 'z': 6}, {'x': 2, 'z': 7}]
        ax = task_func(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(set([text.get_text() for text in ax.legend_.texts]), {'x', 'y', 'z'})
        self.assertEqual(len(ax.lines), 3)
    def test_custom_keys(self):
        data = [{'a': 1, 'b': 10}, {'b': 15, 'c': 6}, {'a': 2, 'c': 7}]
        ax = task_func(data, keys=['a', 'b', 'c'])
        self.assertIsInstance(ax, Axes)
        self.assertEqual(set([text.get_text() for text in ax.legend_.texts]), {'a', 'b', 'c'})
        self.assertEqual(len(ax.lines), 3)
    def test_empty_data_list(self):
        data = []
        ax = task_func(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines), 0)
        self.assertIsNone(ax.legend_)
    def test_single_key_data(self):
        data = [{'x': 1}, {'x': 2}, {'x': 3}]
        ax = task_func(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(set([text.get_text() for text in ax.legend_.texts]), {'x'})
        self.assertEqual(len(ax.lines), 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)