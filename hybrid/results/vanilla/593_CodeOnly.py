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