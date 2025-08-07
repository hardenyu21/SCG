import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(P, T):
    """
    Calculate the product of a matrix 'P' and a 3D tensor 'T' using numpy and visualize the results as a heatmap.

    Parameters:
    P (numpy.ndarray): A 2D numpy array (matrix).
    T (numpy.ndarray): A 3D numpy array (tensor).

    Returns:
    numpy.ndarray: Resultant product after matrix-tensor multiplication.
    matplotlib.axes.Axes: Axes object displaying the heatmap of the 2D result.
    """
    # Ensure P is a 2D array and T is a 3D array
    if P.ndim != 2:
        raise ValueError("P must be a 2D numpy array (matrix).")
    if T.ndim != 3:
        raise ValueError("T must be a 3D numpy array (tensor).")
    
    # Check if the dimensions are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("The number of columns in P must match the first dimension of T.")
    
    # Perform the matrix-tensor multiplication
    # The result will be a 3D array where each 2D slice is the product of P and a 2D slice of T
    result = np.tensordot(P, T, axes=(1, 0))
    
    # Sum over the third dimension to get a 2D result
    result_2d = np.sum(result, axis=2)
    
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(result_2d, annot=True, fmt=".2f", cmap="viridis")
    plt.title("Heatmap of the Resultant 2D Array")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.show()
    
    return result_2d, ax

# Example usage:
# P = np.array([[1, 2], [3, 4]])
# T = np.random.rand(2, 3, 4)
# result_2d, ax = task_func(P, T)