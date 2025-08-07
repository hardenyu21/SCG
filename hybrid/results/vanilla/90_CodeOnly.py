import numpy as np
import math

def task_func(data, target, k):
    # Validate k
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer.")
    
    # Function to calculate the great-circle distance between two points
    def great_circle_distance(lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = 6371 * c  # Radius of Earth in kilometers
        return distance
    
    # Calculate distances from the target to each point in the dataset
    distances = []
    for point in data:
        lat, lon = point
        distance = great_circle_distance(target[0], target[1], lat, lon)
        distances.append((distance, point))
    
    # Sort the distances and get the k nearest neighbors
    distances.sort(key=lambda x: x[0])
    nearest_neighbors = [point for _, point in distances[:k]]
    
    return nearest_neighbors