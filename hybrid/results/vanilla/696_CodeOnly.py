import numpy as np
import math
import random
from random import uniform

def task_func(radius, num_points):
    points = []
    for _ in range(num_points):
        # Generate a random angle
        theta = uniform(0, 2 * math.pi)
        # Generate a random radius, ensuring points are uniformly distributed
        r = radius * math.sqrt(uniform(0, 1))
        # Convert polar coordinates to Cartesian coordinates
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
    return points

# Example usage:
# radius = 5
# num_points = 10
# out = task_func(radius, num_points)
# print(out)