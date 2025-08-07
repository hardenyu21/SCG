import pandas as pd
from texttable import Texttable
import os
import glob

def task_func(data_dir='./data/'):
    # Check if the directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"The specified directory '{data_dir}' does not exist.")
    
    # Find all CSV files in the directory
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    
    # Check if there are any CSV files
    if not csv_files:
        raise ValueError(f"There are no CSV files in the specified directory '{data_dir}'.")
    
    # Sort the CSV files in ascending order
    csv_files.sort()
    
    # Initialize the Texttable
    table = Texttable()
    table.set_cols_align(["l", "r", "r"])
    table.set_cols_valign(["m", "m", "m"])
    table.set_cols_dtype(["t", "i", "i"])
    table.add_rows([["File Name", "Number of Rows", "Number of Columns"]])
    
    # Process each CSV file
    for csv_file in csv_files:
        try:
            # Read the CSV file
            df = pd.read_csv(csv_file)
            
            # Get the number of rows and columns
            num_rows, num_cols = df.shape
            
            # Add a row to the table
            table.add_rows([[os.path.basename(csv_file), num_rows, num_cols]])
        
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError(f"The CSV file '{csv_file}' is empty.")
    
    # Return the string representation of the table
    return table.draw()