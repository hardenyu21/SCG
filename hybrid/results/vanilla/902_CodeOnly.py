import pandas as pd
from collections import Counter

def task_func(d):
    # Initialize a dictionary to hold Counter objects for each key
    result = {'x': Counter(), 'y': Counter(), 'z': Counter()}
    
    # Iterate over each dictionary in the list
    for item in d:
        # Update the Counter for each key if it exists in the current dictionary
        for key in result:
            if key in item:
                result[key].update([item[key]])
    
    return result

# Example usage:
# d = [{'x': 1, 'y': 2}, {'x': 1, 'z': 3}, {'y': 2, 'z': 3}]
# print(task_func(d))