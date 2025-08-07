import csv
import os
import shutil
from datetime import datetime, timedelta
from random import choice

# Constants
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'
BACKUP_DIR = './backup'

def task_func(hours, output_dir=OUTPUT_DIR, backup_dir=BACKUP_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Ensure the backup directory exists
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Generate the file path
    file_name = f'weather_data_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
    file_path = os.path.join(output_dir, file_name)
    
    # Generate weather data
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Condition'])
        
        current_time = datetime.now()
        for _ in range(hours):
            condition = choice(WEATHER_CONDITIONS)
            writer.writerow([current_time.strftime('%Y-%m-%d %H:%M:%S'), condition])
            current_time += timedelta(hours=1)
    
    # Backup the file
    backup_file_path = os.path.join(backup_dir, file_name)
    shutil.copy(file_path, backup_file_path)
    
    return file_path

# Example usage:
# print(task_func(24))