import subprocess
import csv
import os

def task_func(commands_file_path, output_dir_path):
    # Check if the commands file exists
    if not os.path.exists(commands_file_path):
        raise FileNotFoundError(f"The file {commands_file_path} does not exist.")
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    
    output_files = []
    
    # Read commands from the CSV file
    with open(commands_file_path, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if not row:
                continue  # Skip empty rows
            
            command = row[0]
            output_file_path = os.path.join(output_dir_path, f'command_{index}_output.txt')
            output_files.append(output_file_path)
            
            try:
                # Execute the command
                result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
                # Write the output to the file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(result.stdout)
            except subprocess.CalledProcessError as e:
                # Write the error message and exit code to the file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(f"Command failed with exit code {e.returncode}:\n")
                    output_file.write(e.stderr)
    
    return output_files