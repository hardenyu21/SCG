import csv
import os
from datetime import datetime, timedelta
from random import randint
import matplotlib.pyplot as plt
import pandas as pd

# Constants
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate traffic data
    data = []
    current_time = datetime.now().replace(minute=0, second=0, microsecond=0)
    for _ in range(hours):
        row = {'Time': current_time}
        for vehicle in VEHICLE_TYPES:
            row[vehicle] = randint(0, 100)  # Random number of vehicles
        data.append(row)
        current_time += timedelta(hours=1)

    # Save data to CSV
    csv_file_path = os.path.join(output_dir, 'traffic_data.csv')
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Time'] + VEHICLE_TYPES)
        writer.writeheader()
        writer.writerows(data)

    # Plot the data
    df = pd.read_csv(csv_file_path)
    df['Time'] = pd.to_datetime(df['Time'])
    plt.figure(figsize=(10, 6))
    for vehicle in VEHICLE_TYPES:
        plt.plot(df['Time'], df[vehicle], label=vehicle)
    plt.xlabel('Time')
    plt.ylabel('Vehicle Count')
    plt.title('Traffic Data Over Time')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to a file
    plot_file_path = os.path.join(output_dir, 'traffic_plot.png')
    plt.savefig(plot_file_path)

    # Show the plot
    ax = plt.gca()
    plt.show()

    return csv_file_path, ax

# Example usage
# csv_path, ax = task_func(24)
import unittest
from unittest.mock import patch
import shutil
FILE_PATH = os.path.join(OUTPUT_DIR, 'traffic_data.csv')
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up the environment for testing."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
    @patch('matplotlib.pyplot.show')  # Mock plt.show to not render plots
    @patch('csv.writer')  # Mock csv.writer to not actually write files
    @patch('pandas.read_csv')  # Mock pd.read_csv to not read from disk
    @patch(__name__ + '.randint', return_value=25)  # Mock randint to return a fixed value
    def test_dataframe_content(self, mock_randint, mock_read_csv, mock_csv_writer, mock_plt_show):
        mock_read_csv.return_value = pd.DataFrame({
            'Time': ['2021-01-01 00:00:00.000000'],
            'Car': [25], 'Bus': [25], 'Truck': [25], 'Bike': [25]
        })
        file_path, ax = task_func(1)
        self.assertEqual(file_path, FILE_PATH)
        mock_randint.assert_called()  # Ensures randint was called, but not specifics about calls
        mock_read_csv.assert_called_with(FILE_PATH)
        mock_plt_show.assert_called()
    @patch(__name__ + '.pd.read_csv', return_value=pd.DataFrame(columns=['Time'] + VEHICLE_TYPES))
    def test_empty_dataframe_on_zero_hours(self, mock_read_csv):
        """Check for empty DataFrame on zero hours input."""
        _, ax = task_func(0)
        self.assertIsNone(ax)
    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    def test_directory_creation(self, mock_path_exists, mock_makedirs):
        """Ensure directory is created if it does not exist."""
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
        task_func(1)
        mock_makedirs.assert_called_with(os.path.dirname(FILE_PATH))
    @patch(__name__ + '.plt.show')
    def test_plot_generation(self, mock_plt_show):
        """Verify that the plot is generated."""
        task_func(1)
        mock_plt_show.assert_called()
    @patch(__name__ + '.plt.show')  # Mock to skip plot rendering
    def test_task_func_runs_without_error(self, mock_show):
        """Test task_func function to ensure it runs with given hours without raising an error."""
        try:
            task_func(1)  # Attempt to run the function with a simple input
            operation_successful = True
        except Exception:
            operation_successful = False
        self.assertTrue(operation_successful, "task_func should run without errors for given input")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)