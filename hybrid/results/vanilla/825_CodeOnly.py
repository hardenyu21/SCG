import numpy as np
from itertools import product
import string

def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate all possible strings of the given length from the provided alphabets
    all_strings = [''.join(p) for p in product(alphabets, repeat=length)]
    
    # Randomly pick 10 strings from the list of all possible strings
    random_strings = np.random.choice(all_strings, size=10, replace=True)
    
    return list(random_strings)

# Example usage
print(task_func(2, 123, alphabets=['x', 'y', 'z']))