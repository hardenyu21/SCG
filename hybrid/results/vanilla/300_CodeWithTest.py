import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the DataFrame has the required columns
    if 'Date' not in df.columns or 'Value' not in df.columns:
        raise KeyError("The DataFrame must contain 'Date' and 'Value' columns.")
    
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Split 'Value' lists into separate columns
    value_df = df['Value'].apply(pd.Series)
    
    # Calculate Z-scores for each column in the value_df
    zscore_df = value_df.apply(zscore, axis=0)
    
    # Replace the original 'Value' column with the Z-scores
    df = df.drop(columns=['Value']).join(zscore_df)
    
    # Create a box plot for Z-scores over time
    fig, ax = plt.subplots(figsize=(10, 6))
    df.set_index('Date').boxplot(ax=ax)
    ax.set_title("Z-Scores Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Z-Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return df, fig
import unittest
import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
    
    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['Date', 'Value'])
        with self.assertRaises(Exception):
            task_func(df)
        plt.close()
    def test_typical_data(self):
        df = pd.DataFrame([[self.fake.date(), [self.fake.random_number(digits=2) for _ in range(3)]] for _ in range(5)],
                          columns=['Date', 'Value'])
        zscore_df, fig = task_func(df)
        self.assertEqual(zscore_df.shape, (5, 4))
        self.assertIsInstance(fig, plt.Figure)
        self.assertEqual(len(fig.axes), 1)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), 'Z-Scores Over Time')
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Z-Score')
        plt.close()
    def test_nan_values(self):
        df = pd.DataFrame([['2021-01-01', [5, np.nan, 7]], ['2021-01-02', [np.nan, 9, 10]]], columns=['Date', 'Value'])
        zscore_df, fig = task_func(df)
        self.assertEqual(zscore_df.shape, (2, 4))
        self.assertIsInstance(fig, plt.Figure)
        plt.close()
    def test_single_row_data(self):
        df = pd.DataFrame([[self.fake.date(), [self.fake.random_number(digits=2) for _ in range(3)]]],
                          columns=['Date', 'Value'])
        zscore_df, fig = task_func(df)
        self.assertEqual(zscore_df.shape, (1, 4))
        self.assertIsInstance(fig, plt.Figure)
        plt.close()
    def test_non_numeric_values(self):
        df = pd.DataFrame([[self.fake.date(), [self.fake.word() for _ in range(3)]] for _ in range(5)],
                          columns=['Date', 'Value'])
        with self.assertRaises(Exception):
            task_func(df)
        plt.close()
    def test_large_dataset(self):
        df = pd.DataFrame([[self.fake.date(), [self.fake.random_number(digits=2) for _ in range(10)]] for _ in range(100)],
                          columns=['Date', 'Value'])
        zscore_df, fig = task_func(df)
        self.assertEqual(zscore_df.shape, (100, 11))
        self.assertIsInstance(fig, plt.Figure)
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)