import numpy as np
from itertools import chain

def task_func(L):
    # Flatten the nested list using chain.from_iterable
    flat_list = list(chain.from_iterable(L))
    
    # Calculate the mean
    mean_value = np.mean(flat_list)
    
    # Calculate the variance
    variance_value = np.var(flat_list)
    
    # Return the results in a dictionary
    return {'mean': mean_value, 'variance': variance_value}

# Example usage:
# L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = task_func(L)
# print(result)  # Output: {'mean': 5.0, 'variance': 6.666666666666667}