import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def task_func(points, seed=0):
    # Validate input
    if not isinstance(points, np.ndarray):
        raise TypeError("Input points must be a numpy array.")
    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("Input points must be a 2D array with shape (n, 2).")
    
    # Apply jittering to avoid degenerate cases
    np.random.seed(seed)
    jitter = np.random.normal(scale=1e-10, size=points.shape)
    points_jittered = points + jitter
    
    # Compute Voronoi diagram
    vor = Voronoi(points_jittered)
    
    # Plot the Voronoi diagram
    fig, ax = plt.subplots()
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=2, line_alpha=0.6, point_size=2)
    ax.set_title('Voronoi Diagram')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal', 'box')
    
    # Return the Voronoi object and the axes
    return vor, ax

# Example usage:
# points = np.array([[0, 0], [1, 4], [2, 3], [4, 1], [1, 1], [2, 2], [5, 3]])
# vor, ax = task_func(points)
# plt.show()