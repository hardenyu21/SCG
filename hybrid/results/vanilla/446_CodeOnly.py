import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def task_func(n_samples=100, centers=3, n_features=2, random_seed=42):
    # Generate isotropic Gaussian blobs for clustering
    X, y = make_blobs(n_samples=n_samples, centers=centers, n_features=n_features, random_state=random_seed)
    
    # Create a scatter plot of the blobs
    fig, ax = plt.subplots()
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k', s=50)
    
    # Add a legend
    legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
    ax.add_artist(legend1)
    
    # Set plot title and labels
    ax.set_title('Isotropic Gaussian Blobs')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    
    # Show the plot
    plt.show()
    
    # Return the data and the Axes object
    return X, y, ax

# Example usage
X, y, ax = task_func()