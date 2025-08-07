import os
import pandas as pd
import numpy as np

def task_func(data_dir: str, csv_file: str) -> pd.DataFrame:
    # Construct the full file path
    file_path = os.path.join(data_dir, csv_file)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {csv_file} does not exist in the directory {data_dir}.")
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # If the DataFrame is empty, return it as is
    if df.empty:
        return df
    
    # Replace NaN values in numeric columns with the mean of the column
    for column in df.select_dtypes(include=[np.number]).columns:
        mean_value = df[column].mean()
        df[column].fillna(mean_value, inplace=True)
    
    return df