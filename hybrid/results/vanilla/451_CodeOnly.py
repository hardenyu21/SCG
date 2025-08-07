import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    # Set random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate a high-dimensional dataset
    data = np.random.randn(N_SAMPLES, N_FEATURES)
    
    # Apply PCA to reduce dimensionality
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)
    
    # Calculate the covariance matrix of the transformed data
    covariance_matrix = np.cov(transformed_data, rowvar=False)
    
    # Plot the heatmap of the covariance matrix if n_components > 1
    heatmap_axes = None
    if n_components > 1:
        plt.figure(figsize=(8, 6))
        heatmap_axes = sns.heatmap(covariance_matrix, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Covariance Matrix of Transformed Data')
        plt.show()
    
    return transformed_data, heatmap_axes

# Example usage:
# transformed_data, heatmap_axes = task_func(n_components=3, N_SAMPLES=500, N_FEATURES=50, random_seed=42)