import random
from itertools import combinations
import math

def task_func(n):
    if n < 2:
        return None
    
    # Generate n random dots within the unit square
    dots = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(n)]
    
    # Initialize variables to store the minimum distance and the closest pair
    min_distance = float('inf')
    closest_pair = None
    
    # Iterate over all pairs of dots
    for (x1, y1), (x2, y2) in combinations(dots, 2):
        # Calculate the Euclidean distance between the two dots
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        # Update the minimum distance and closest pair if a closer pair is found
        if distance < min_distance:
            min_distance = distance
            closest_pair = ((x1, y1), (x2, y2))
    
    return closest_pair