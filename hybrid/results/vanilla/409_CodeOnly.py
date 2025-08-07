import os
import pandas as pd
import numpy as np

def task_func(excel_file_path, file_name, column_name):
    # Construct the full file path
    full_file_path = os.path.join(excel_file_path, file_name)
    
    # Check if the file exists
    if not os.path.exists(full_file_path):
        raise FileNotFoundError(f"The file {file_name} does not exist at the specified path {excel_file_path}.")
    
    # Load the Excel file into a DataFrame
    try:
        df = pd.read_excel(full_file_path)
    except Exception as e:
        raise ValueError(f"Error reading the Excel file: {e}")
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The column '{column_name}' is not found in the Excel file.")
    
    # Extract the data from the specified column
    data = df[column_name]
    
    # Calculate mean, median, and standard deviation
    mean_value = np.mean(data)
    median_value = np.median(data)
    std_dev_value = np.std(data, ddof=0)  # Population standard deviation
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'standard_deviation': std_dev_value
    }