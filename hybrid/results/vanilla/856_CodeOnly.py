from functools import reduce
from itertools import combinations
import numpy as np

def task_func(shape=(3, 3), low=1, high=10, seed=None):
    if high <= low:
        raise ValueError("high must be greater than low")
    
    if seed is not None:
        np.random.seed(seed)
    
    # Generate the matrix with random numbers within the specified range
    matrix = np.random.randint(low, high, size=shape)
    
    # Flatten the matrix to a 1D array to easily generate all possible pairs
    flat_matrix = matrix.flatten()
    
    # Generate all possible combinations of two numbers from the matrix
    pairs = combinations(flat_matrix, 2)
    
    # Calculate the sum of the products of all pairs
    sum_of_products = sum(a * b for a, b in pairs)
    
    return sum_of_products, matrix

# Example usage
result = task_func((5, 4), seed=1)
print(result)