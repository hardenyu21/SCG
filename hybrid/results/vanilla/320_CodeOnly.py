import subprocess
import os
import random

def task_func(directory, file_list):
    if not file_list:
        return None

    # Select a random file from the list
    random_file = random.choice(file_list)

    # Construct the full path to the file
    file_path = os.path.join(directory, random_file)

    # Check if the file exists and is executable
    if not os.path.isfile(file_path) or not os.access(file_path, os.X_OK):
        return None

    # Run the file as a subprocess
    try:
        result = subprocess.run(file_path, check=False)
        return result.returncode
    except Exception as e:
        print(f"An error occurred while running the file: {e}")
        return None