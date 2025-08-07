import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def task_func(array, seed=None):
    # Check if the input array is 2D
    if array.ndim != 2:
        raise ValueError("Input array must be 2D.")
    
    # Check if the array is empty or has no features
    if array.size == 0 or array.shape[1] == 0:
        return pd.DataFrame(columns=['PC1', 'PC2'])
    
    # Shuffle the columns of the array randomly
    if seed is not None:
        np.random.seed(seed)
    shuffled_indices = np.random.permutation(array.shape[1])
    shuffled_array = array[:, shuffled_indices]
    
    # Determine the number of components for PCA
    n_components = min(2, shuffled_array.shape[1])
    
    # Perform PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(shuffled_array)
    
    # Create a DataFrame with the principal components
    if n_components == 1:
        # If only one component, add a column of zeros for PC2
        principal_components = np.column_stack((principal_components, np.zeros(principal_components.shape[0])))
    
    df = pd.DataFrame(principal_components, columns=['PC1', 'PC2'])
    
    return df