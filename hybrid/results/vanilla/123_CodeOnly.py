import pandas as pd
import os
import glob

def task_func(my_list, file_dir='./data_files/', file_ext='.csv'):
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise TypeError("The first argument must be a list.")
    
    # Add the element '12' to the list
    my_list.append('12')
    
    # Convert all elements in the list to integers and calculate the sum
    try:
        num_files_to_concat = sum(int(x) for x in my_list)
    except ValueError:
        raise ValueError("All elements in the list must be convertible to integers.")
    
    # Construct the file pattern
    file_pattern = os.path.join(file_dir, '*' + file_ext)
    
    # Find all CSV files in the directory
    csv_files = glob.glob(file_pattern)
    
    # Check if any files are found
    if not csv_files:
        raise FileNotFoundError("No files found in the specified directory.")
    
    # Limit the number of files to concatenate based on the sum of the list
    csv_files_to_concat = csv_files[:num_files_to_concat]
    
    # Concatenate the CSV files into a single DataFrame
    dataframes = []
    for file in csv_files_to_concat:
        df = pd.read_csv(file)
        dataframes.append(df)
    
    concatenated_df = pd.concat(dataframes, ignore_index=True)
    
    return concatenated_df