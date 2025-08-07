import csv
import random
from datetime import datetime, timedelta

# Constants
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}

def task_func(file_name="data.csv"):
    # Get the current date
    current_date = datetime.now().date()
    
    # Prepare data for each hour of the current day
    data = []
    for hour in range(24):
        hour_data = {
            'Time': current_date + timedelta(hours=hour),
            'Temperature': random.uniform(*RANGE['Temperature']),
            'Humidity': random.uniform(*RANGE['Humidity']),
            'Pressure': random.uniform(*RANGE['Pressure'])
        }
        data.append(hour_data)
    
    # Write data to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Time'] + DATA)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    
    return file_name

# Example usage
file_path = task_func()
print(f"CSV file created at: {file_path}")
import unittest
import os
import csv
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup for the test cases, creating a mock file name
        self.mock_file_name = "test_task_func_data.csv"
        
    def tearDown(self):
        # Cleanup after each test, removing the generated file if it exists
        if os.path.exists(self.mock_file_name):
            os.remove(self.mock_file_name)
    def test_case_1(self):
        # Testing default file name
        random.seed(0)
        returned_file = task_func(self.mock_file_name)
        self.assertTrue(os.path.exists(returned_file))
        
    def test_case_2(self):
        # Testing custom file name
        random.seed(0)
        returned_file = task_func(self.mock_file_name)
        self.assertTrue(os.path.exists(returned_file))
        
    def test_case_3(self):
        # Testing content structure of the CSV file
        random.seed(0)
        task_func(self.mock_file_name)
        with open(self.mock_file_name, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, ['Time', 'Temperature', 'Humidity', 'Pressure'])
            
    def test_case_4(self):
        # Testing content data ranges of the CSV file
        random.seed(0)
        task_func(self.mock_file_name)
        with open(self.mock_file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                temp, humidity, pressure = float(row[1]), float(row[2]), float(row[3])
                self.assertTrue(-50 <= temp <= 50)
                self.assertTrue(0 <= humidity <= 100)
                self.assertTrue(980 <= pressure <= 1040)
                
    def test_case_5(self):
        # Testing number of rows (24 hours + header)
        random.seed(0)
        task_func(self.mock_file_name)
        with open(self.mock_file_name, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 25)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)