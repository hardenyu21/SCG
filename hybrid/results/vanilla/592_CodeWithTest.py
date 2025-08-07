import csv
import os
from datetime import datetime, timedelta
from random import uniform

# Constants
SENSORS = ['Temperature', 'Humidity', 'Pressure']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the file path
    file_path = os.path.join(output_dir, 'sensor_data.csv')

    # Generate data
    data = []
    current_time = datetime.now()
    for _ in range(hours):
        # Generate random sensor data
        temperature = uniform(15.0, 35.0)  # Random temperature between 15°C and 35°C
        humidity = uniform(30.0, 80.0)     # Random humidity between 30% and 80%
        pressure = uniform(980.0, 1050.0)  # Random pressure between 980 hPa and 1050 hPa

        # Append the data to the list
        data.append([current_time, temperature, humidity, pressure])

        # Increment the time by one hour
        current_time += timedelta(hours=1)

    # Write data to CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Time', 'Temperature', 'Humidity', 'Pressure'])
        # Write the data
        writer.writerows(data)

    print(f"Sensor data for {hours} hours has been saved to {file_path}")

# Example usage
task_func(24)
import unittest
import os
import shutil
FILE_PATH = os.path.join(OUTPUT_DIR, 'sensor_data.csv')
class TestCases(unittest.TestCase):
    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
    def test_csv_file_creation(self):
        """Test if the CSV file is successfully created."""
        task_func(1)
        self.assertTrue(os.path.exists(FILE_PATH))
    def test_csv_file_rows(self):
        """Test if the CSV file contains the correct number of rows for 24 hours."""
        task_func(24)
        with open(FILE_PATH, 'r') as f:
            self.assertEqual(len(f.readlines()), 25)  # Including header
    def test_csv_file_header(self):
        """Test if the CSV file header matches the expected sensors."""
        task_func(0)
        with open(FILE_PATH, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['Time', 'Temperature', 'Humidity', 'Pressure'])
    def test_file_path_return(self):
        """Test if the correct file path is returned."""
        file_path = task_func(1)
        self.assertEqual(file_path, FILE_PATH)
    def test_no_hours_data(self):
        """Test sensor data generation with 0 hours."""
        task_func(0)
        with open(FILE_PATH, 'r') as f:
            self.assertEqual(len(f.readlines()), 1)  # Only header row expected


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)