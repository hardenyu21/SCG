from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    # Handle the case where the list is empty or contains only one point
    if len(points) < 2:
        return []
    
    # Normalize points to ensure each is a tuple of two numbers
    normalized_points = [(x, x) if isinstance(x, (int, float)) else x for x in points]
    
    # Calculate Euclidean distances between consecutive points
    distances = [
        distance.euclidean(p1, p2)
        for p1, p2 in zip_longest(normalized_points, normalized_points[1:])
    ]
    
    return distances

# Example usage
print(task_func([(1, 2), (4), (-1.2, 4)]))  # Output: [3.605551275463989, 5.2]