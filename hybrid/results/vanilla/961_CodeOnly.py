import os
from collections import Counter

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise OSError(f"The specified directory '{directory}' does not exist.")
    
    # Initialize a Counter object to store the counts of each file extension
    file_counter = Counter()
    
    # Walk through the directory recursively
    for root, _, files in os.walk(directory):
        for file in files:
            # Get the file extension
            file_extension = os.path.splitext(file)[1]
            
            # Check if the file extension is in the specified extensions
            if file_extension in extensions:
                # Increment the count for this file extension
                file_counter[file_extension] += 1
    
    # If keep_zero is False, remove extensions with zero count
    if not keep_zero:
        file_counter = Counter({ext: count for ext, count in file_counter.items() if count > 0})
    
    return file_counter