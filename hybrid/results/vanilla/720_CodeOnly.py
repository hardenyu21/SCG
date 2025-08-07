import os
import csv
import random
from datetime import datetime

def task_func():
    # Define the directory and file path
    directory = "task_func_data"
    file_path = os.path.join(directory, "Output.txt")
    
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Generate random sensor data
    data = []
    for _ in range(10):  # Generate 10 data points
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)
        data.append([timestamp, temperature, humidity])
    
    # Write the data to the CSV file in append mode
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # Write header if the file is empty
            writer.writerow(["Timestamp", "Temperature", "Humidity"])
        writer.writerows(data)
    
    # Return the path to the CSV file
    print(f"Data written to {file_path}")
    
    # Delete the file after use
    os.remove(file_path)
    print(f"File {file_path} deleted.")
    
    return file_path

# Example usage
task_func()