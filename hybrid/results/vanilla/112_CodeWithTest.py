import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a pandas DataFrame and contains the 'Status' column
    if not isinstance(df, pd.DataFrame) or 'Status' not in df.columns:
        raise ValueError("Input must be a pandas DataFrame with a 'Status' column.")
    
    # Count the occurrences of each status
    status_counts = df['Status'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Return the Axes object
    return ax
import unittest
from random import choice
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        self.df = pd.DataFrame({'Status': [choice(['Pending', 'In Progress', 'Completed', 'Cancelled']) for _ in range(100)]})
    
    def test_return_value(self):
        ax = task_func(self.df)
        # Assuming 'ax' is the Axes object returned by your function 'task_func'
        # Retrieve the pie chart wedges and texts
        wedges, texts, autotexts = ax.patches, ax.texts, ax.texts[1::2]
        # Extract the labels and percentages
        labels = [text.get_text() for text in texts
                  ]
        status_dict = {labels[i]: labels[i + 1] for i in range(0, len(labels), 2)}
        expect = {'In Progress': '29.0%', 'Pending': '27.0%', 'Completed': '24.0%', 'Cancelled': '20.0%'}
        self.assertEqual(status_dict, expect, "contents should match the expected output")
    def test_return_type(self):
        ax = task_func(self.df)
        self.assertIsInstance(ax, plt.Axes)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame({'A': [1, 2], 'B': [3, 4]}))
    def test_plot_title(self):
        ax = task_func(self.df)
        self.assertEqual(ax.get_title(), 'Status Distribution')
    def test_pie_labels(self):
        ax = task_func(self.df)
        labels = [text.get_text() for text in ax.texts]
        for status in ['Pending', 'In Progress', 'Completed', 'Cancelled']:
            self.assertIn(status, labels)
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)