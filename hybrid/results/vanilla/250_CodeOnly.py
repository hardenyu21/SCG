import numpy as np
import itertools
import json

def task_func(data_list, json_file_name="mean_values.json"):
    # Flatten the list of lists to handle any nested lists
    flattened_data = list(itertools.chain.from_iterable(data_list))
    
    # Filter out non-numeric values
    numeric_values = [value for value in flattened_data if isinstance(value, (int, float))]
    
    # Calculate the mean of the numeric values
    if numeric_values:
        mean_value = np.mean(numeric_values)
    else:
        mean_value = 0  # or handle the case where there are no numeric values
    
    # Create a dictionary with the mean value for each position
    result = {f'Position {i}': mean_value for i in range(len(data_list))}
    
    # Export the results to a JSON file if a file name is provided
    if json_file_name:
        with open(json_file_name, 'w') as json_file:
            json.dump(result, json_file, indent=4)
    
    return result

# Example usage:
data = [
    [1, 2, 3],
    [4, 5, 'a'],
    [7, 8, 9]
]

mean_values = task_func(data)
print(mean_values)