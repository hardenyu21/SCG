import numpy as np
from sklearn.decomposition import PCA

def task_func(tuples_list, n_components):
    # Convert the list of tuples into a numpy array
    data = np.array(tuples_list)
    
    # Initialize PCA with the specified number of components
    pca = PCA(n_components=n_components)
    
    # Fit PCA on the data and transform it
    transformed_data = pca.fit_transform(data)
    
    return transformed_data