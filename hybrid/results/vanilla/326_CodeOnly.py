import subprocess
import os
import glob

def task_func(directory_path):
    # List to store the results
    results = []

    # Ensure the directory path is absolute
    directory_path = os.path.abspath(directory_path)

    # Find all .bat files in the given directory
    bat_files = glob.glob(os.path.join(directory_path, '*.bat'))

    # Iterate over each .bat file
    for bat_file in bat_files:
        try:
            # Run the .bat file and capture the exit code
            result = subprocess.run(bat_file, shell=True, check=False)
            exit_code = result.returncode
        except Exception as e:
            # If an error occurs, set the exit code to None
            exit_code = None

        # Append the file name and exit code to the results list
        results.append((os.path.basename(bat_file), exit_code))

    return results