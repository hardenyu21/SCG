import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path, col1_name="column1", col2_name="column2"):
    # Read data from the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Group the DataFrame by 'col1_name' and calculate the mean of 'col2_name' for each group
    grouped_mean = df.groupby(col1_name)[col2_name].mean()
    
    # Create a bar plot
    fig, ax = plt.subplots()
    grouped_mean.plot(kind='bar', ax=ax)
    
    # Set the title and labels
    ax.set_title(f"Mean of {col2_name} Grouped by {col1_name}")
    ax.set_xlabel(col1_name)
    ax.set_ylabel(f"Mean of {col2_name}")
    
    # Return the Axes object for further customization
    return ax
import unittest
import pandas as pd
from unittest.mock import patch
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for the function."""
    def setUp(self):
        # Define mock data
        self.data = {
            "sample_data": pd.DataFrame(
                {"column1": ["A", "A", "B", "B"], "column2": [1, 2, 3, 4]}
            ),
            "different_data": pd.DataFrame(
                {"column1": ["C", "C", "D", "D"], "column2": [5, 6, 7, 8]}
            ),
            "missing_values": pd.DataFrame(
                {"column1": ["A", "A", "B", "B"], "column2": [1, None, 3, None]}
            ),
            "different_columns": pd.DataFrame(
                {"col1": ["E", "E", "F", "F"], "col2": [9, 10, 11, 12]}
            ),
            "single_group_data": pd.DataFrame(
                {"column1": ["A", "A", "A"], "column2": [1, 2, 3]}
            ),
            "non_numeric_data": pd.DataFrame(
                {"column1": ["A", "B", "C"], "column2": ["x", "y", "z"]}
            ),
        }
    @patch("pandas.read_csv")
    def test_bar_plot(self, mock_read_csv):
        """Test standard bar plot generation with sample data."""
        mock_read_csv.return_value = self.data["sample_data"]
        ax = task_func("any_path.csv", "column1", "column2")
        self.check_plot(ax, "sample_data", "column1", "column2")
    @patch("pandas.read_csv")
    def test_different_data(self, mock_read_csv):
        """Test bar plot with different data set."""
        mock_read_csv.return_value = self.data["different_data"]
        ax = task_func("any_path.csv", "column1", "column2")
        self.check_plot(ax, "different_data", "column1", "column2")
    @patch("pandas.read_csv")
    def test_missing_values(self, mock_read_csv):
        """Test bar plot with missing values in data."""
        mock_read_csv.return_value = self.data["missing_values"]
        ax = task_func("any_path.csv", "column1", "column2")
        self.check_plot(ax, "missing_values", "column1", "column2")
    @patch("pandas.read_csv")
    def test_different_column_names(self, mock_read_csv):
        """Test bar plot with different column names."""
        mock_read_csv.return_value = self.data["different_columns"]
        ax = task_func("any_path.csv", "col1", "col2")
        self.check_plot(ax, "different_columns", "col1", "col2")
    @patch("pandas.read_csv")
    def test_single_group_data(self, mock_read_csv):
        """Test bar plot with data containing only a single group."""
        mock_read_csv.return_value = self.data["single_group_data"]
        ax = task_func("any_path.csv", "column1", "column2")
        self.check_plot(ax, "single_group_data", "column1", "column2")
    @patch("pandas.read_csv")
    def test_non_numeric_aggregation_column(self, mock_read_csv):
        """Test bar plot with non-numeric data in the aggregation column."""
        mock_read_csv.return_value = self.data["non_numeric_data"]
        with self.assertRaises(TypeError):
            task_func("any_path.csv", "column1", "column2")
    def check_plot(self, ax, data_key, col1, col2):
        """Check the generated bar plot."""
        # Use the correct DataFrame for expected calculations
        df = self.data[data_key]
        # Common assertions for checking plot
        expected_title = f"Mean of {col2} Grouped by {col1}"
        self.assertEqual(ax.get_title(), expected_title)
        self.assertEqual(ax.get_xlabel(), col1)
        self.assertEqual(ax.get_ylabel(), f"Mean of {col2}")
        # Check the bars in the plot
        bars = ax.patches
        bar_heights = [bar.get_height() for bar in bars]
        expected_means = df.groupby(col1)[col2].mean().values
        self.assertListEqual(bar_heights, list(expected_means))
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)