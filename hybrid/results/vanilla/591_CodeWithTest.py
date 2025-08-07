from datetime import datetime, timedelta
from random import randint
import matplotlib.pyplot as plt
import pandas as pd

TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'

def task_func(hours, file_path=FILE_PATH):
    # Initialize data dictionary
    data = {
        'Time': [],
        'Temperature': [],
        'Category': []
    }
    
    # Generate temperature data for the specified number of hours
    current_time = datetime.now()
    for _ in range(hours):
        # Generate a random temperature between -10 and 40 degrees Celsius
        temperature = randint(-10, 40)
        
        # Determine the temperature category
        if temperature < 10:
            category = TEMP_CATEGORIES[0]  # Cold
        elif temperature < 30:
            category = TEMP_CATEGORIES[1]  # Normal
        else:
            category = TEMP_CATEGORIES[2]  # Hot
        
        # Append data to the dictionary
        data['Time'].append(current_time.strftime('%Y-%m-%d %H:%M:%S'))
        data['Temperature'].append(temperature)
        data['Category'].append(category)
        
        # Increment the time by one hour
        current_time += timedelta(hours=1)
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    
    # Plot the temperature data
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'], marker='o', linestyle='-')
    ax.set_title('Temperature Data Over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the file path and the plot object
    return file_path, ax

# Example usage:
# file_path, ax = task_func(24)
# plt.show()
import unittest
import os
class TestCases(unittest.TestCase):
    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
    def test_case_1(self):
        # Testing with 1 hour
        file_path, ax = task_func(1)
        self.assertEqual(file_path, FILE_PATH)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 1)
    def test_case_2(self):
        # Testing with 24 hours
        file_path, ax = task_func(24)
        self.assertEqual(file_path, FILE_PATH)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 24)
    def test_case_3(self):
        # Testing with 120 hours
        file_path, ax = task_func(120)
        self.assertEqual(file_path, FILE_PATH)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 120)
    def test_case_4(self):
        # Testing with a custom file path
        file_path, ax = task_func(24, FILE_PATH)
        self.assertEqual(file_path, FILE_PATH)
        self.assertTrue(os.path.exists(FILE_PATH))
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), 24)
    def test_case_5(self):
        # Testing the categories in the generated CSV file
        file_path, ax = task_func(24, FILE_PATH)
        df = pd.read_csv(file_path)
        categories = df['Category'].unique().tolist()
        for cat in categories:
            self.assertIn(cat, ['Cold', 'Normal', 'Hot'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)