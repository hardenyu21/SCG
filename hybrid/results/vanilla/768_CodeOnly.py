import re
import os
import glob

def task_func(dir_path):
    # Check if the directory exists
    if not os.path.exists(dir_path):
        raise ValueError(f"The directory '{dir_path}' does not exist.")
    
    # Dictionary to store the count of "error" occurrences
    error_count = {}
    
    # Use glob to find all .txt files in the directory and its subdirectories
    txt_files = glob.glob(os.path.join(dir_path, '**', '*.txt'), recursive=True)
    
    # Regular expression to find occurrences of "error" (case insensitive)
    error_pattern = re.compile(r'\berror\b', re.IGNORECASE)
    
    # Iterate over each text file
    for file_path in txt_files:
        # Calculate the relative file path
        relative_path = os.path.relpath(file_path, dir_path)
        
        # Initialize the count for this file
        count = 0
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Find all occurrences of "error" in the line
                matches = error_pattern.findall(line)
                # Increment the count by the number of matches
                count += len(matches)
        
        # Store the count in the dictionary
        error_count[relative_path] = count
    
    return error_count