import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(input_file):
    # Read the JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Initialize a defaultdict to store lists of values for each key
    values_dict = defaultdict(list)
    
    # Collect values for each key
    for entry in data:
        for key, value in entry.items():
            values_dict[key].append(value)
    
    # Calculate mean and median for each key
    result = {}
    for key, values in values_dict.items():
        mean_value = np.mean(values)
        median_value = np.median(values)
        result[key] = {'mean': mean_value, 'median': median_value}
    
    # Create bar charts for each key
    plots = []
    for key, stats in result.items():
        fig, ax = plt.subplots()
        ax.bar(['Mean', 'Median'], [stats['mean'], stats['median']])
        ax.set_title(f'Statistics for {key}')
        ax.set_ylabel('Value')
        plots.append(ax)
    
    # Return the results and plots
    return result, plots

# Example usage:
# result, plots = task_func('data.json')
# for plot in plots:
#     plot.show()