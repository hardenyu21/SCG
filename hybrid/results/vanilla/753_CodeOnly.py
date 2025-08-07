import math
import random
import statistics

# Constants
RADIUS = 5

def task_func(n):
    distances = []
    
    for _ in range(n):
        # Generate a random angle
        theta = random.uniform(0, 2 * math.pi)
        
        # Generate a random radius, considering the uniform distribution of points
        r = RADIUS * math.sqrt(random.uniform(0, 1))
        
        # Calculate the distance from the center (which is the radius itself)
        distance = r
        
        # Store the distance
        distances.append(distance)
    
    # Calculate the average distance
    average_distance = statistics.mean(distances)
    
    return average_distance

# Example usage:
# print(task_func(1000))