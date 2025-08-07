import subprocess
import csv
import glob
import random
import os

def task_func(file):
    # Check if the file exists and is a CSV file
    if not os.path.isfile(file) or not file.endswith('.csv'):
        return []

    try:
        # Use the 'split' command to divide the CSV file into smaller files
        # Each file will have a prefix 'split_'
        subprocess.run(['split', '-l', '100', file, 'split_'], check=True)

        # Get a list of all split files
        split_files = glob.glob('split_*')

        # Shuffle the lines in each split file
        for split_file in split_files:
            with open(split_file, 'r', newline='') as f:
                reader = csv.reader(f)
                lines = list(reader)

            random.shuffle(lines)

            with open(split_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(lines)

        return split_files

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while splitting the file: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []