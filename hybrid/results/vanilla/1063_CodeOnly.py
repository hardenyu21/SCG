from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def task_func(arr):
    # Sum the rows of the 2D array
    row_sums = np.sum(arr, axis=1).reshape(-1, 1)
    
    # Perform PCA on the row sums
    pca = PCA(n_components=1)
    pca.fit(row_sums)
    
    # Get the explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Plot the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, alpha=0.7, align='center')
    ax.set_title("Explained Variance Ratio of Principal Components")
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    
    # Show the plot
    plt.show()
    
    return ax