import pandas as pd
import numpy as np

def task_func(list_of_lists):
    series_list = []
    for sub_list in list_of_lists:
        # Create a list of integers from 1 to the length of the sub-list
        values = list(range(1, len(sub_list) + 1))
        # Shuffle the list of integers
        np.random.shuffle(values)
        # Create a pandas Series with the shuffled values and the sub-list as the index
        series = pd.Series(values, index=sub_list)
        # Append the Series to the list
        series_list.append(series)
    return series_list

# Example usage:
# list_of_lists = [['a', 'b', 'c'], ['x', 'y'], ['m', 'n', 'o', 'p']]
# series_list = task_func(list_of_lists)
# for series in series_list:
#     print(series)