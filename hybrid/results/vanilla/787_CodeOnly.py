import numpy as np
from itertools import combinations

def task_func(array1, array2):
    # Check if the input arrays have different lengths
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length.")
    
    # If the arrays are empty, return 0
    if len(array1) == 0:
        return 0.0
    
    # Combine elements from both arrays to form points
    points = list(zip(array1, array2))
    
    # Initialize the maximum distance
    max_distance = 0.0
    
    # Calculate the Euclidean distance between all pairs of points
    for (x1, y1), (x2, y2) in combinations(points, 2):
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if distance > max_distance:
            max_distance = distance
    
    return max_distance