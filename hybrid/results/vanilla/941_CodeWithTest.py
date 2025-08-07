import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate a date range starting from the given date
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate random sales data
    # Here, we assume sales follow a normal distribution with a mean of 100 and a standard deviation of 20
    sales = np.random.normal(loc=100, scale=20, size=periods)
    
    # Create a DataFrame with the generated dates and sales
    forecast_df = pd.DataFrame({'Date': dates, 'Sales': sales})
    
    # Plot the sales forecast
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(forecast_df['Date'], forecast_df['Sales'], marker='o', linestyle='-')
    ax.set_title('Sales Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the DataFrame and the Axes object
    return forecast_df, ax

# Example usage:
# df, ax = task_func('2023-01-01', 12, 'M')
# plt.show()
import unittest
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.random_seed = 42
    def test_basic_forecast(self):
        df, ax = task_func('2021-01-01', 5, 'WOM-2FRI', self.random_seed)
        self.assertEqual(len(df), 5)
        self.assertTrue(all(df.columns == ['Sales']))
        self.assertEqual(ax.get_title(), 'Sales Forecast')
    def test_monthly_forecast(self):
        df, ax = task_func('2022-01-01', 3, 'M', self.random_seed)
        self.assertEqual(len(df), 3)
        self.assertTrue(all(df.columns == ['Sales']))
    def test_quarterly_forecast(self):
        df, ax = task_func('2020-01-01', 4, 'Q', self.random_seed)
        self.assertEqual(len(df), 4)
        self.assertTrue(all(df.columns == ['Sales']))
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            task_func('2021-13-01', 5, 'M', self.random_seed)
    def test_negative_periods(self):
        with self.assertRaises(ValueError):
            task_func('2021-01-01', -5, 'M', self.random_seed)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)