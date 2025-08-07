import numpy as np
from functools import reduce

def task_func(list_of_pairs):
    # Extract the second value from each tuple
    second_values = [pair[1] for pair in list_of_pairs]
    
    # Calculate the product of the second values
    product = reduce(lambda x, y: x * y, second_values)
    
    # Return the product as a single-element numpy array
    return np.array([product])

# Example usage:
# list_of_pairs = [(1, 2), (3, 4), (5, 6)]
# result = task_func(list_of_pairs)
# print(result)  # Output: array([48])