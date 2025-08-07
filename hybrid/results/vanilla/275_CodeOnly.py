import numpy as np
from itertools import combinations

def task_func(n):
    if n < 1:
        raise ValueError("This function will raise Value Error if the input n is less than 1.")
    
    # Generate all possible integer pairs within the range of 1 to n
    pairs = list(combinations(range(1, n + 1), 2))
    
    return pairs

# Example usage:
# print(task_func(3))  # Output: [(1, 2), (1, 3), (2, 3)]