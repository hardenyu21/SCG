import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(P, T, tensor_shape=(3, 3, 3)):
    # Ensure P is a 2D matrix and T is a 3D tensor
    if P.ndim != 2:
        raise ValueError("P must be a 2D matrix.")
    if T.ndim != 3:
        raise ValueError("T must be a 3D tensor.")
    
    # Reshape T to match the expected shape
    T = T.reshape(tensor_shape)
    
    # Calculate the product of matrix P and tensor T
    # P has shape (N, M) and T has shape (M, K, L)
    # We need to perform a matrix multiplication along the second axis of T
    # Resulting in a 3D array of shape (N, K, L)
    product = np.tensordot(P, T, axes=(1, 0))
    
    # Flatten the 3D array to 2D for PCA
    # The resulting shape will be (N, K*L)
    flattened_product = product.reshape(P.shape[0], -1)
    
    # Apply PCA to reduce the dimensionality to 2
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(flattened_product)
    
    # Visualize the PCA result
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1])
    ax.set_title('PCA Result Visualization')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    
    # Return the PCA result and the plot axis
    return pca_result, ax

# Example usage:
# P = np.random.rand(5, 3)
# T = np.random.rand(3, 3, 3)
# pca_result, ax = task_func(P, T)
# plt.show()