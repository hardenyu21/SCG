import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:
    # Compile the regex pattern for matching filenames
    regex = re.compile(pattern)
    
    # Initialize a list to store the names of new files
    new_files = []
    
    # Iterate over all files in the specified directory
    for file in os.listdir(directory):
        # Check if the file matches the pattern
        match = regex.match(file)
        if match:
            # Extract the base name from the matched pattern
            base_name = match.group(1)
            
            # Define the new filename by appending '_new' before the extension
            new_filename = f"{base_name}_new.csv"
            
            # Construct full file paths
            old_file_path = Path(directory) / file
            new_file_path = Path(directory) / new_filename
            
            # Read the content from the old file
            with open(old_file_path, mode='r', newline='') as old_file:
                reader = csv.reader(old_file)
                data = list(reader)
            
            # Write the content to the new file
            with open(new_file_path, mode='w', newline='') as new_file:
                writer = csv.writer(new_file)
                writer.writerows(data)
            
            # Add the new filename to the list
            new_files.append(new_filename)
    
    return new_files