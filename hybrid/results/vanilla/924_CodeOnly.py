import pandas as pd
import os
import sys

def task_func(file_path: str, column_name: str) -> pd.DataFrame:
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The column {column_name} does not exist in the DataFrame.")
    
    # Replace all occurrences of '\n' with '<br>' in the specified column
    df[column_name] = df[column_name].str.replace('\n', '<br>', regex=False)
    
    # Return the cleaned DataFrame
    return df