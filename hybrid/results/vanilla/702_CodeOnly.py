import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    # Initialize PCA with 2 components
    pca = PCA(n_components=2)
    
    # Fit and transform the data
    principal_components = pca.fit_transform(df)
    
    # Create a DataFrame with the first two principal components
    df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    
    return df_pca