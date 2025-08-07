import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(x, y, labels):
    # Combine x and y into a single dataset
    data = np.column_stack((x, y))
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data)
    
    # Create a scatter plot of the principal components
    fig, ax = plt.subplots()
    scatter = ax.scatter(principal_components[:, 0], principal_components[:, 1], c='blue', alpha=0.5)
    
    # Annotate each point with its label
    for i, label in enumerate(labels):
        ax.annotate(label, (principal_components[i, 0], principal_components[i, 1]))
    
    # Set plot labels
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA of x and y values')
    
    # Return the figure object
    return fig