import matplotlib.pyplot as plt
import pandas as pd

def task_func(temperatures):
    # Check if the input is a DataFrame and not empty
    if not isinstance(temperatures, pd.DataFrame) or temperatures.empty:
        raise ValueError("The input DataFrame is not in the expected format or is empty.")
    
    # Check if the DataFrame has the expected columns
    expected_columns = ['Date', 'Temperature (°C)']
    if not all(column in temperatures.columns for column in expected_columns):
        raise ValueError("The DataFrame must contain 'Date' and 'Temperature (°C)' columns.")
    
    # Convert the 'Date' column to datetime format
    temperatures['Date'] = pd.to_datetime(temperatures['Date'])
    
    # Sort the DataFrame by date
    temperatures = temperatures.sort_values(by='Date')
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(temperatures['Date'], temperatures['Temperature (°C)'], marker='o', linestyle='-')
    
    # Set the plot properties
    ax.set_xlabel('Date', fontname='Arial')
    ax.set_ylabel('Temperature (°C)', fontname='Arial')
    ax.set_title('Daily Temperatures in New York', fontname='Arial')
    
    # Rotate date labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent clipping of tick-labels
    plt.tight_layout()
    
    # Return the Axes object
    return ax
import unittest
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temperatures = pd.DataFrame({
            'temperature': [random.randint(-10, 30) for _ in range(365)],
            'date': pd.date_range(start='01-01-2023', periods=365, tz='America/New_York')
        }).set_index('date')
    def test_basic_functionality(self):
        ax = task_func(self.temperatures)
        self.assertIsInstance(ax, plt.Axes)
    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame())
    def test_incorrect_dataframe(self):
        incorrect_df = pd.DataFrame({'temp': [20, 21], 'time': [datetime.now(), datetime.now()]})
        with self.assertRaises(ValueError):
            task_func(incorrect_df)
    def test_data_on_plot(self):
        ax = task_func(self.temperatures)
        self.assertEqual(len(ax.get_lines()[0].get_xdata()), 365)
        self.assertEqual(len(ax.get_lines()[0].get_ydata()), 365)
    def test_plot_labels_and_title(self):
        ax = task_func(self.temperatures)
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Temperature (°C)')
        self.assertEqual(ax.get_title(), 'Daily Temperatures in New York')
    
    def test_value_consistency(self):
        ax = task_func(self.temperatures)
        line = ax.get_lines()[0]
        plot_dates = line.get_xdata()
        plot_temperatures = line.get_ydata()
        for date, temperature in zip(plot_dates, plot_temperatures):
            self.assertAlmostEqual(temperature, self.temperatures.at[pd.Timestamp(date), 'temperature'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)