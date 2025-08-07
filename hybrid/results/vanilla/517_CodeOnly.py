import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    # Convert the 2D list into a pandas DataFrame
    df = pd.DataFrame(array)
    
    # Initialize PCA with 2 components and a fixed random seed for reproducibility
    pca = PCA(n_components=2, random_state=random_seed)
    
    # Fit and transform the data using PCA
    pca_transformed = pca.fit_transform(df)
    
    # Return the original DataFrame and the transformed data
    return df, pca_transformed