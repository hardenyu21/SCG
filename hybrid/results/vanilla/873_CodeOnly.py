import csv
import os

def task_func(data, file_path, headers):
    if file_path is None:
        raise ValueError("file_path cannot be None.")
    
    # Ensure the file path is absolute
    absolute_path = os.path.abspath(file_path)
    
    # Open the file in write mode
    with open(absolute_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the headers
        writer.writerow(headers)
        
        # Write each row, filling missing values with None
        for row in data:
            # Extend the row with None if it has fewer elements than headers
            extended_row = list(row) + [None] * (len(headers) - len(row))
            writer.writerow(extended_row)
    
    return absolute_path