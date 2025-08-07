import collections
import numpy as np
import pandas as pd

def task_func(file_name):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_name)
    
    # Check if the DataFrame is empty
    if df.empty:
        return {}
    
    # Dictionary to store the most common values for each column
    most_common_values = {}
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Count the occurrences of each value in the column
        value_counts = df[column].value_counts()
        
        # If the column is empty, skip it
        if value_counts.empty:
            continue
        
        # Get the most common value(s)
        most_common = value_counts.idxmax()
        
        # If there are multiple values with the same highest count, sort them alphabetically
        if value_counts[most_common] == value_counts.nlargest(2).iloc[-1]:
            most_common = value_counts[value_counts == value_counts[most_common]].index.tolist()
            most_common.sort()
            most_common = most_common[0]
        
        # Store the most common value in the dictionary
        most_common_values[column] = most_common
    
    return most_common_values