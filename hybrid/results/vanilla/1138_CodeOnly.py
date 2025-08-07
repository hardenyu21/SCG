import numpy as np
import itertools

def task_func(matrix):
    # Flatten the 2D array and sort it
    sorted_array = np.sort(matrix, axis=None)
    
    # Find all unique combinations of two elements from the sorted array
    unique_combinations = list(itertools.combinations(sorted_array, 2))
    
    # Return the sorted array and the list of unique combinations
    return sorted_array, unique_combinations

# Example usage:
# matrix = np.array([[3, 1], [4, 2]])
# sorted_array, unique_combinations = task_func(matrix)
# print("Sorted Array:", sorted_array)
# print("Unique Combinations:", unique_combinations)