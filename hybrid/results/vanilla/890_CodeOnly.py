import os
import random
import pandas as pd

def task_func(data_dir,
              csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
              seed=None,
              num_records=10):
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Randomly select one of the provided csv_files
    selected_file = random.choice(csv_files)
    
    # Construct the full file path
    file_path = os.path.join(data_dir, selected_file)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {selected_file} does not exist in the directory {data_dir}.")
    
    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        # Return an empty DataFrame if the file is empty
        return selected_file, pd.DataFrame()
    
    # Check if the DataFrame is empty
    if df.empty:
        return selected_file, pd.DataFrame()
    
    # Randomly select a certain number of records from the DataFrame
    selected_records = df.sample(n=min(num_records, len(df)), random_state=seed)
    
    return selected_file, selected_records