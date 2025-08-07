import urllib.request
import os
import csv
import collections

def task_func(url, column_name, csv_file_path):
    try:
        # Download the CSV file from the given URL
        urllib.request.urlretrieve(url, csv_file_path)
        
        # Initialize a counter to count occurrences of each value in the specified column
        value_counter = collections.Counter()
        
        # Open the CSV file and read its contents
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Check if the specified column exists in the CSV file
            if column_name not in reader.fieldnames:
                raise ValueError(f"The provided column_name '{column_name}' does not exist in the CSV file.")
            
            # Count occurrences of each value in the specified column
            for row in reader:
                value = row[column_name]
                value_counter[value] += 1
        
        # Delete the downloaded CSV file after processing
        os.remove(csv_file_path)
        
        # Return the dictionary of value counts
        return dict(value_counter)
    
    except Exception as e:
        # If an error occurs, delete the downloaded file if it exists
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)
        # Re-raise the exception
        raise e