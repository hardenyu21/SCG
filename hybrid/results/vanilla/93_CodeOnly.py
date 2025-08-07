import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Check if n_components is a positive integer
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer.")
    
    # Perform PCA
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)
    
    # Create a DataFrame for the transformed data
    columns = [f'PC{i+1}' for i in range(n_components)]
    df_transformed = pd.DataFrame(transformed_data, columns=columns)
    
    # Generate a scatter plot
    fig, ax = plt.subplots()
    if n_components == 1:
        ax.scatter(df_transformed[columns[0]], np.zeros_like(df_transformed[columns[0]]))
        ax.set_xlabel(columns[0])
        ax.set_yticks([])
    elif n_components == 2:
        ax.scatter(df_transformed[columns[0]], df_transformed[columns[1]])
        ax.set_xlabel(columns[0])
        ax.set_ylabel(columns[1])
    else:
        raise ValueError("Scatter plot is only supported for 1 or 2 principal components.")
    
    plt.title('PCA Scatter Plot')
    plt.grid(True)
    
    # Return the transformed DataFrame and the Axes object
    return df_transformed, ax