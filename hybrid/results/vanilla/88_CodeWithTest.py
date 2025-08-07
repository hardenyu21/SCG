import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(start_date, end_date, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Generate a list of dates from start_date to end_date, inclusive
    date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    
    # Generate random sales data for each date
    sales_data = np.random.randint(0, 501, size=len(date_range))
    
    # Create a DataFrame with the date and sales data
    df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    
    # Plot the sales data over time
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Sales'], marker='o', linestyle='-')
    ax.set_title('Sales Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# df, ax = task_func('2023-01-01', '2023-01-10')
# plt.show()
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.start_date = datetime(2021, 1, 1)
        self.end_date = datetime(2021, 1, 10)
    def test_random_reproducibility(self):
        df1, _ = task_func(self.start_date, self.end_date, 42)
        df2, _ = task_func(self.start_date, self.end_date, 42)
        pd.testing.assert_frame_equal(df1, df2)
    def test_dataframe_structure(self):
        df, _ = task_func(self.start_date, self.end_date)
        self.assertListEqual(list(df.columns), ["Date", "Sales"])
        self.assertEqual(len(df), (self.end_date - self.start_date).days + 1)
    def test_sales_values_range(self):
        df, _ = task_func(self.start_date, self.end_date)
        self.assertTrue(df["Sales"].between(0, 500).all())
    def test_different_seeds_produce_different_data(self):
        df1, _ = task_func(self.start_date, self.end_date, 42)
        df2, _ = task_func(self.start_date, self.end_date, 43)
        self.assertFalse(df1.equals(df2))
    
    def test_values(self):
        df1, _ = task_func(self.start_date, self.end_date, 42)
        df_list = df1.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        
        expect = ['2021-01-01 00:00:00,102', '2021-01-02 00:00:00,435', '2021-01-03 00:00:00,348', '2021-01-04 00:00:00,270', '2021-01-05 00:00:00,106', '2021-01-06 00:00:00,71', '2021-01-07 00:00:00,188', '2021-01-08 00:00:00,20', '2021-01-09 00:00:00,102', '2021-01-10 00:00:00,121']
        
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)