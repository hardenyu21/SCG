import os
import pandas as pd
from dateutil.parser import parse
import matplotlib.pyplot as plt

OUTPUT_DIR = './output'

def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Convert the date column to datetime objects
    df[date_column] = df[date_column].apply(parse)
    
    # Extract the year from the datetime objects
    df['year'] = df[date_column].dt.year
    
    # Plot the histogram of the year distribution
    fig, ax = plt.subplots()
    ax.hist(df['year'], bins=range(df['year'].min(), df['year'].max() + 2), edgecolor='black')
    
    # Set labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Frequency')
    ax.set_title('Year Distribution of Dates')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# ax = task_func(csv_path='path_to_your_csv_file.csv', date_column='your_date_column_name')
import unittest
import shutil
import os
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.output_dir = OUTPUT_DIR
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        # Prepare CSV files for testing
        self.valid_data_csv = os.path.join(self.output_dir, 'valid_data.csv')
        with open(self.valid_data_csv, 'w') as f:
            f.write("date\n2020-01-01\n2021-02-02")
        self.empty_data_csv = os.path.join(self.output_dir, 'empty_data.csv')
        open(self.empty_data_csv, 'w').close()  # Create an empty file
        # No need to create an invalid data CSV because parsing errors are tested dynamically
        self.different_column_data_csv = os.path.join(self.output_dir, 'different_column_data.csv')
        with open(self.different_column_data_csv, 'w') as f:
            f.write("different_date_column\n2020-01-01\n2021-02-02")
    def tearDown(self):
        shutil.rmtree(self.output_dir, ignore_errors=True)
    def test_valid_data(self):
        """Test with valid date data."""
        histogram_plot = task_func(self.valid_data_csv, 'date')
        self.assertIsInstance(histogram_plot, plt.Axes)
    def test_empty_file(self):
        """Test with an empty CSV file."""
        with self.assertRaises(ValueError):  # Assuming pandas raises a ValueError for an empty CSV
            task_func(self.empty_data_csv, 'date')
    def test_nonexistent_file(self):
        """Test with a nonexistent CSV file path."""
        nonexistent_csv = os.path.join(self.output_dir, 'nonexistent.csv')
        with self.assertRaises(FileNotFoundError):
            task_func(nonexistent_csv, 'date')
    def test_different_date_column(self):
        """Test using a different date column name."""
        histogram_plot = task_func(self.different_column_data_csv, 'different_date_column')
        self.assertIsInstance(histogram_plot, plt.Axes)
    def test_invalid_data(self):
        """Dynamically test with invalid date strings; expecting the function to handle errors gracefully."""
        invalid_data_csv = os.path.join(self.output_dir, 'invalid_data.csv')
        with open(invalid_data_csv, 'w') as f:
            f.write("date\nnot-a-date\n2021-13-01")
        with self.assertRaises(ValueError):
            task_func(invalid_data_csv, 'date')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)