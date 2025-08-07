import numpy as np
from collections import defaultdict
import json
import csv

# Constants
def task_func(input_file, output_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a dictionary to store lists of values for each key
    values_dict = defaultdict(list)
    
    # Populate the dictionary with values from the JSON data
    for entry in data:
        for key, value in entry.items():
            values_dict[key].append(value)
    
    # Calculate mean and median for each key
    results = {}
    for key, values in values_dict.items():
        mean_value = np.mean(values)
        median_value = np.median(values)
        results[key] = {'mean': mean_value, 'median': median_value}
    
    # Write the results to a CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Field', 'Mean', 'Median'])
        # Write the data
        for key, stats in results.items():
            writer.writerow([key, stats['mean'], stats['median']])
    
    return results

# Example usage:
# results = task_func('input.json', 'output.csv')