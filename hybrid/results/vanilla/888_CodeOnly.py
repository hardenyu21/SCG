import pandas as pd
import os

def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    # Check if the list of files is empty
    if not csv_files:
        return pd.DataFrame()
    
    # Initialize an empty list to store DataFrames
    dataframes = []
    
    # Iterate over the list of CSV files
    for file_name in csv_files:
        # Construct the full file path
        file_path = os.path.join(data_dir, file_name)
        
        # Check if the file exists
        if os.path.isfile(file_path):
            # Read the CSV file into a DataFrame and append to the list
            df = pd.read_csv(file_path)
            dataframes.append(df)
        else:
            print(f"Warning: File {file_path} does not exist and will be skipped.")
    
    # Concatenate all DataFrames in the list into a single DataFrame
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    return merged_df