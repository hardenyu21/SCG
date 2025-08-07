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