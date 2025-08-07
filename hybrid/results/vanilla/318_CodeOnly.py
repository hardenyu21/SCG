import random
import math
import matplotlib.pyplot as plt

def task_func(points_count=1000, radius=1):
    # Generate random points within a circle
    points = []
    for _ in range(points_count):
        # Generate a random angle
        theta = random.uniform(0, 2 * math.pi)
        # Generate a random radius, ensuring uniform distribution
        r = radius * math.sqrt(random.uniform(0, 1))
        # Convert polar coordinates to Cartesian coordinates
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
    
    # Unpack the points into x and y coordinates
    x_coords, y_coords = zip(*points)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x_coords, y_coords)
    
    # Set the aspect ratio to 'equal'
    ax.set_aspect('equal')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax