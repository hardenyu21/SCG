import collections
import pandas as pd
import os

def task_func(my_tuple, path_csv_files):
    # Initialize a dictionary to store the results
    result = {column: collections.defaultdict(int) for column in my_tuple}
    
    # Iterate over each file in the specified directory
    for filename in os.listdir(path_csv_files):
        if filename.endswith('.csv'):
            file_path = os.path.join(path_csv_files, filename)
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Iterate over each specified column
            for column in my_tuple:
                if column in df.columns:
                    # Count occurrences of each value in the column
                    value_counts = df[column].value_counts()
                    # Update the result dictionary with these counts
                    for value, count in value_counts.items():
                        result[column][value] += count
    
    # Convert defaultdicts to regular dicts for the final output
    result = {column: dict(counts) for column, counts in result.items()}
    
    return result