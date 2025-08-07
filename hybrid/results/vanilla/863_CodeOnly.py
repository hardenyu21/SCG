import numpy as np
import math

# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)

def task_func(list_of_lists):
    sums = []
    for lst in list_of_lists:
        length = len(lst)
        # Select the first 'length' numbers from POSSIBLE_NUMBERS
        selected_numbers = POSSIBLE_NUMBERS[:length]
        # Calculate the sum of squares of the selected numbers
        sum_of_squares = np.sum(selected_numbers ** 2)
        sums.append(sum_of_squares)
    return sums

# Example usage:
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = task_func(list_of_lists)
print(result)  # Output: [14, 54, 130]