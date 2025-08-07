import matplotlib.pyplot as plt
import numpy as np

def task_func(n, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random points
    x = np.random.rand(n)
    y = np.random.rand(n)
    
    # Create a list of (x, y) tuples
    points = list(zip(x, y))
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    
    # Set the title and labels
    ax.set_title("Scatter plot of random points")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    
    # Return the plot and the list of points
    return fig, points

# Example usage:
# fig, points = task_func(10)
# plt.show()