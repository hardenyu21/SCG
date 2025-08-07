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