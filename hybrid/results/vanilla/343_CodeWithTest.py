import pandas as pd
import matplotlib.pyplot as plt

# Constants for pie chart colors
COLORS = ['r', 'g', 'b', 'y', 'm']

def task_func(df, col, title=None):
    # Validate input
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df must be a DataFrame.")
    if df.empty:
        raise ValueError("The DataFrame must not be empty.")
    if col not in df.columns:
        raise ValueError(f"The DataFrame must contain the column '{col}'.")
    
    # Count unique values in the specified column
    value_counts = df[col].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(value_counts, labels=value_counts.index, colors=COLORS[:len(value_counts)], autopct='%1.1f%%', startangle=90)
    
    # Set the title if provided
    if title:
        ax.set_title(title)
    
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')
    
    # Return the Axes object
    return ax
import unittest
from unittest.mock import patch
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup fake data for testing
        self.df = pd.DataFrame({
            'fruit': ['apple', 'banana', 'orange', 'apple', 'banana', 'banana'],
            'quantity': [10, 15, 5, 10, 15, 15]
        })
    def test_valid_input(self):
        # Test with valid input and column
        ax = task_func(self.df, 'fruit')
        self.assertIsInstance(ax, plt.Axes)
        plt.close()
    def test_nonexistent_column(self):
        # Test with a nonexistent column
        with self.assertRaises(Exception):
            task_func(self.df, 'color')
        plt.close()
    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        with self.assertRaises(Exception):
            task_func(pd.DataFrame(), 'fruit')
        plt.close()
    def test_pie_chart_title(self):
        # Test with a title for the pie chart
        title = "Distribution of Fruits"
        ax = task_func(self.df, 'fruit', title=title)
        self.assertEqual(ax.get_title(), title)
        plt.close()
    def test_numeric_data(self):
        # Test with numeric data
        ax = task_func(self.df, 'quantity')
        self.assertIsInstance(ax, plt.Axes)
        plt.close()
        
    def test_color_length(self):
        # Test if the number of colors matches the number of unique values
        ax = task_func(self.df, 'fruit')
        try:
            self.assertEqual(3 <= len(ax.patches) <= 5, True)
        except:
            self
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)