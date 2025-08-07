import numpy as np
import itertools

def task_func(data_list):
    if not data_list:
        return []

    # Determine the maximum length of tuples
    max_length = max(len(t) for t in data_list)

    # Pad tuples with None to make them the same length
    padded_data = [t + (None,) * (max_length - len(t)) for t in data_list]

    # Unzip the padded data
    unzipped_data = list(itertools.zip_longest(*padded_data))

    # Calculate the mean for each position
    means = []
    for position in unzipped_data:
        numeric_values = [x for x in position if isinstance(x, (int, float))]
        if numeric_values:
            means.append(np.mean(numeric_values))
        else:
            means.append(np.nan)

    return means