import os
import os.path
import csv
import collections

# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):
    # Dictionary to store file sizes
    file_sizes = collections.defaultdict(int)

    # Walk through the directory
    for root, dirs, files in os.walk(my_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes[file_path] = file_size

    # Write the file sizes to a CSV file
    csv_file_path = os.path.join(my_path, FILE_NAME)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['File Path', 'File Size (bytes)'])
        for file_path, size in file_sizes.items():
            csv_writer.writerow([file_path, size])

    # Return the path of the CSV file
    return csv_file_path