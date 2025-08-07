import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def task_func(data, date_format, country, country_codes=None):
    # Validate inputs
    if not isinstance(data, pd.DataFrame):
        raise ValueError("The 'data' parameter must be a pandas DataFrame.")
    if not isinstance(date_format, str):
        raise ValueError("The 'date_format' parameter must be a string.")
    if country_codes is not None and not isinstance(country_codes, dict):
        raise ValueError("The 'country_codes' parameter must be a dictionary.")
    if country_codes is not None and country not in country_codes:
        raise ValueError(f"The 'country' parameter '{country}' is not in 'country_codes'.")

    # Convert the data column to datetime format
    try:
        data['date'] = pd.to_datetime(data['date'], format=date_format)
    except Exception as e:
        raise ValueError(f"Error converting dates: {e}")

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(data['date'].dt.date, bins=30, color='blue', edgecolor='black')
    ax.set_title('Date Distribution')
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Date')

    # Return the Axes object
    return ax
import unittest
import pandas as pd
import matplotlib.axes
import numpy as np
from datetime import datetime
class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({'dates': ['01/01/2000', '01/02/2000', '02/03/2000', '04/05/2000', '06/07/2000']})
    def test_valid_data(self):
        ax = task_func(self.data, '%d/%m/%Y', 'Russia')
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.get_title(), 'Date Distribution')
    def test_non_existing_country(self):
        with self.assertRaises(ValueError):
            task_func(self.data, '%d/%m/%Y', 'Mars')
    def test_invalid_data_type(self):
        with self.assertRaises(ValueError):
            task_func("Not a DataFrame", '%d/%m/%Y', 'Russia')
    def test_invalid_date_format_type(self):
        with self.assertRaises(ValueError):
            task_func(self.data, 123, 'Russia')
    def test_custom_country_codes(self):
        custom_codes = {'Mars': 'en_US'}
        ax = task_func(self.data, '%d/%m/%Y', 'Mars', country_codes=custom_codes)
        self.assertEqual(ax.get_title(), 'Date Distribution')
    
    def test_histogram_values(self):
        ax = task_func(self.data, '%d/%m/%Y', 'Russia')
        # Convert dates to datetime objects for frequency calculation
        converted_dates = pd.to_datetime(self.data['dates'], format='%d/%m/%Y')
        expected_counts = [1, 1, 0, 1, 0, 0, 1, 0, 0, 1]
    
        # Get actual histogram data
        n, bins, patches = ax.hist(converted_dates)
        # Compare the actual frequencies with the expected frequencies
        np.testing.assert_array_almost_equal(n, expected_counts)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)