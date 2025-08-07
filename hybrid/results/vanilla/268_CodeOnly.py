import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    # Initialize an empty dictionary
    result_dict = collections.defaultdict(list)
    
    # Generate the specified number of keys
    keys = random.sample(LETTERS, n_keys)
    
    # Assign consecutive integers to each key
    for i in range(n_values):
        key = keys[i % n_keys]  # Cycle through keys if n_values > n_keys
        result_dict[key].append(i + 1)
    
    # Convert defaultdict to a regular dict before returning
    return dict(result_dict)

# Example usage:
# print(task_func(5, 10))