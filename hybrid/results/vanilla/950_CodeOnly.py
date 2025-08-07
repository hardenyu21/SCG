import numpy as np
from scipy.linalg import svd

def task_func(rows=3, columns=2, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a matrix of random values with specified dimensions
    matrix = np.random.rand(rows, columns)
    
    # Perform Singular Value Decomposition (SVD)
    U, s, Vh = svd(matrix)
    
    # Return the results as a tuple
    return U, s, Vh

# Example usage:
# U, s, Vh = task_func(3, 2, 0)
# print("U:\n", U)
# print("s:\n", s)
# print("Vh:\n", Vh)