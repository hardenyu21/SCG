import os
import re
import pandas as pd

def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    # Compile the regex pattern for efficiency
    regex = re.compile(pattern)
    
    # List to store matched file paths
    matched_paths = []
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file name matches the regex pattern
            if regex.match(file):
                # Construct the full file path
                full_path = os.path.join(root, file)
                # Append the matched path to the list
                matched_paths.append(full_path)
    
    # Create a DataFrame from the matched paths
    df = pd.DataFrame(matched_paths, columns=['File Path'])
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    
    # Return the DataFrame
    return df