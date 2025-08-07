import re
import os
import glob
import natsort
import pandas as pd

def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The specified directory '{directory}' does not exist.")
    
    # Find all files matching the pattern
    file_paths = glob.glob(os.path.join(directory, file_pattern))
    
    # Sort the file paths naturally
    file_paths = natsort.natsorted(file_paths)
    
    # Check if any files were found
    if not file_paths:
        raise ValueError(f"No files matching the pattern '{file_pattern}' were found in the directory '{directory}'.")
    
    # Prepare a list to store the extracted data
    data = []
    
    # Compile the regex pattern
    pattern = re.compile(regex)
    
    # Iterate over each file
    for file_path in file_paths:
        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Find all numeric data in the file
        numeric_data = pattern.findall(content)
        
        # Convert numeric data to integers
        numeric_data = [int(num) for num in numeric_data]
        
        # Append the filename and numeric data to the list
        data.append({'Filename': os.path.basename(file_path), 'Numeric Data': numeric_data})
    
    # Create a DataFrame from the collected data
    df = pd.DataFrame(data)
    
    return df