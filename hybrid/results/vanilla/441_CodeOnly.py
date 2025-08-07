import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def task_func(P, T):
    # Ensure P is a 2D matrix and T is a 3D tensor
    if P.ndim != 2 or T.ndim != 3:
        raise ValueError("P must be a 2D matrix and T must be a 3D tensor.")
    
    # Calculate the product using Einstein summation
    # Assuming P has shape (M, N) and T has shape (N, 3, K)
    # The result will have shape (M, 3, K)
    result = np.einsum('ij,jkl->ikl', P, T)
    
    # Flatten the result to (M, 3) for visualization
    result_flat = result.reshape(result.shape[0], -1)
    
    # Plotting the result in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot each point in the result
    for i in range(result_flat.shape[0]):
        ax.scatter(result_flat[i, 0], result_flat[i, 1], result_flat[i, 2], label=f'Point {i}')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    
    plt.show()
    
    return result_flat, ax

# Example usage:
# P = np.array([[1, 2], [3, 4]])
# T = np.random.rand(2, 3, 5)
# result, ax = task_func(P, T)