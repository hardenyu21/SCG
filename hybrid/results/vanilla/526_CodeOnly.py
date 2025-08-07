import json
import pandas as pd
import numpy as np
from collections import defaultdict

def task_func(input_file="data.json"):
    # Load data from JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a dictionary to store lists of values for each key
    values_dict = defaultdict(list)
    
    # Iterate over each dictionary in the list
    for entry in data:
        for key, value in entry.items():
            # Check if the value is numeric
            if isinstance(value, (int, float)):
                values_dict[key].append(value)
    
    # Calculate mean and median for each key
    results = []
    for key, values in values_dict.items():
        mean_value = np.mean(values)
        median_value = np.median(values)
        results.append({'variable': key, 'mean': mean_value, 'median': median_value})
    
    # Convert results to a DataFrame
    df = pd.DataFrame(results).set_index('variable').sort_index()
    
    return df

# Example usage:
# df = task_func("data.json")
# print(df)