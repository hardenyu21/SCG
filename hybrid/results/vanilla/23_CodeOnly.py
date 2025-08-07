import numpy as np
from itertools import zip_longest

def task_func(l1, l2, THRESHOLD=0.5):
    # Combine elements from l1 and l2 alternately
    combined = []
    for a, b in zip_longest(l1, l2):
        if a is not None:
            combined.append(a)
        if b is not None:
            combined.append(b)
    
    # Calculate the absolute difference from the threshold
    differences = [abs(x - THRESHOLD) for x in combined]
    
    # Find the element with the minimum difference
    min_diff_index = np.argmin(differences)
    closest_element = combined[min_diff_index]
    
    return closest_element

# Example usage:
l1 = [0.1, 0.6, 0.9]
l2 = [0.3, 0.8]
print(task_func(l1, l2))  # Output: 0.6