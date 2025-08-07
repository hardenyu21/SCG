import numpy as np
import itertools

def task_func(dimension, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Create a 2D numpy array with random integers between 1 and 100
    matrix = np.random.randint(1, 101, size=dimension)
    
    # Flatten the matrix into a list
    flat_list = list(itertools.chain.from_iterable(matrix))
    
    # Return the tuple containing the matrix and the flat list
    return matrix, flat_list

# Example usage:
# matrix, flat_list = task_func((3, 4))
# print("Matrix:\n", matrix)
# print("Flat List:", flat_list)