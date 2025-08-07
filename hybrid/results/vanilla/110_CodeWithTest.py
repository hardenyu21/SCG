import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the DataFrame has the required columns
    if 'Date' not in df.columns or 'Sales' not in df.columns:
        raise ValueError("DataFrame must contain 'Date' and 'Sales' columns.")
    
    # Check if the DataFrame has any data to plot
    if df.empty:
        raise ValueError("DataFrame has no data to plot.")
    
    # Convert 'Date' column to datetime if it's not already
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort the DataFrame by 'Date'
    df = df.sort_values(by='Date')
    
    # Plot the line chart
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], marker='o', linestyle='-')
    
    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Daily Turnover Line Chart')
    
    # Rotate date labels for better readability
    plt.xticks(rotation=45)
    
    # Return the Axes object
    return ax
import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', periods=10),
            'Sales': np.random.randint(100, 2000, size=10)
        })
    def test_return_type(self):
    # Adjusted to include more data points
        np.random.seed(42)
        large_df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', periods=30),
            'Sales': np.random.randint(100, 2000, size=30)
        })
        ax = task_func(large_df)
        self.assertIsInstance(ax, plt.Axes)
        
    def test_value(self):
        # Adjusted to include more data points
        ax = task_func(self.df)
        # Retrieve the line plot data
        # Assuming 'ax' is the Axes object returned by your function 'task_func'
        # Retrieve the line plot data
        line = ax.get_lines()[0]  # Get the first (and likely only) line plot
        sales = line.get_ydata()
        actual_sales = [str(int(sale)) for sale in sales]
        expect = ['1226', '1559', '960', '1394', '1230', '1195', '1824', '1144', '1738', '221']
        self.assertEqual(actual_sales, expect, "DataFrame contents should match the expected output")
        
    def test_plot_title_and_labels(self):
        # Adjusted to include more data points
        np.random.seed(42)
        large_df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', periods=30),
            'Sales': np.random.randint(100, 2000, size=30)
        })
        ax = task_func(large_df)
        self.assertEqual(ax.get_title(), 'Daily Turnover')
        self.assertEqual(ax.get_ylabel(), 'Sales')
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}))
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame({'Date': [], 'Sales': []}))
    def test_date_conversion(self):
        df_with_string_dates = self.df.copy()
        df_with_string_dates['Date'] = df_with_string_dates['Date'].dt.strftime('%Y-%m-%d')
        ax = task_func(df_with_string_dates)
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)