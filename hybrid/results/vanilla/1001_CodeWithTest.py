import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path: str):
    # Read data from the CSV file
    data = pd.read_csv(csv_file_path)
    
    # Normalize the 'column1' data
    column1 = data['column1']
    normalized_column1 = (column1 - column1.min()) / (column1.max() - column1.min())
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(normalized_column1)
    
    # Set the title with formatted strings
    title = f"{'Plot Title':<20}:{'Normalized Column 1':>20}"
    ax.set_title(title)
    
    # Set the x-label with formatted strings
    xlabel = f"{'Index':<20}:{'Normalized Value':>20}"
    ax.set_xlabel(xlabel)
    
    # Set the y-label with formatted strings
    ylabel = f"{'Frequency':<20}:{'Normalized Value':>20}"
    ax.set_ylabel(ylabel)
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax
import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    @patch("pandas.read_csv")
    def test_title_format(self, mock_read_csv):
        """Test that the function returns the correct title."""
        # Mocking the DataFrame
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = task_func("dummy_path")
        expected_title = "          Plot Title :  Normalized Column 1"
        self.assertEqual(ax.get_title(), expected_title)
    @patch("pandas.read_csv")
    def test_xlabel_format(self, mock_read_csv):
        """Test that the function returns the correct xlabel."""
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = task_func("dummy_path")
        expected_xlabel = "               Index :     Normalized Value"
        self.assertEqual(ax.get_xlabel(), expected_xlabel)
    @patch("pandas.read_csv")
    def test_ylabel_format(self, mock_read_csv):
        """Test that the function returns the correct ylabel."""
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = task_func("dummy_path")
        expected_ylabel = "           Frequency :     Normalized Value"
        self.assertEqual(ax.get_ylabel(), expected_ylabel)
    @patch("pandas.read_csv")
    def test_data_points_length(self, mock_read_csv):
        """Test that the function returns the correct number of data points."""
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = task_func("dummy_path")
        line = ax.get_lines()[0]
        self.assertEqual(len(line.get_data()[1]), 10)
    @patch("pandas.read_csv")
    def test_data_points_range(self, mock_read_csv):
        """Test that the function returns the correct data points."""
        mock_data = pd.DataFrame({"column1": np.random.rand(10)})
        mock_read_csv.return_value = mock_data
        ax = task_func("dummy_path")
        line = ax.get_lines()[0]
        data_points = line.get_data()[1]
        self.assertTrue(all(-3 <= point <= 3 for point in data_points))
    def tearDown(self):
        plt.clf()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)