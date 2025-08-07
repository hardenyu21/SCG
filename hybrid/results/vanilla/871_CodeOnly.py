import numpy as np
import itertools

def task_func(data_list, file_name):
    if not data_list:
        with open(file_name, 'w') as file:
            pass
        return []

    # Determine the maximum length of tuples (excluding the first element)
    max_length = max(len(t) for t in data_list) - 1

    # Initialize a list to store the means
    means = []

    # Iterate over each position (excluding the first element)
    for pos in range(1, max_length + 1):
        # Extract the values at the current position, filling missing values with np.nan
        values = [t[pos] if pos < len(t) else np.nan for t in data_list]

        # Calculate the mean, ignoring np.nan values
        mean_value = np.nanmean(values)

        # Append the mean to the list
        means.append(mean_value)

        # Write the result to the file
        with open(file_name, 'a') as file:
            file.write(f'Position {pos}: {mean_value}\n')

    return means