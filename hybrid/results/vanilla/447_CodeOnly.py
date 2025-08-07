import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, n_components=2, random_state=None):
    # Initialize PCA with the specified number of components
    pca = PCA(n_components=n_components, random_state=random_state)
    
    # Fit and transform the data
    transformed_data = pca.fit_transform(data)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    
    if n_components == 1:
        # For 1D data, plot along the X-axis with Y-values set to zero
        ax.scatter(transformed_data, np.zeros_like(transformed_data), alpha=0.7)
        ax.set_xlabel('Principal Component 1')
        ax.set_yticks([])  # Hide y-ticks for 1D plot
    else:
        # For 2D or more data, plot the first two principal components
        ax.scatter(transformed_data[:, 0], transformed_data[:, 1], alpha=0.7)
        ax.set_xlabel('Principal Component 1')
        ax.set_ylabel('Principal Component 2')
    
    # Set plot title
    ax.set_title('PCA Visualization')
    
    # Return the transformed data and the Axes object
    return {
        "transformed_data": transformed_data,
        "ax": ax
    }