import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        return 0, 0
    
    # Convert lists in the DataFrame into separate columns
    # Assuming the DataFrame has a column named 'numbers' containing lists
    df_expanded = df.drop('numbers', axis=1).join(df['numbers'].apply(pd.Series))
    
    # Perform PCA
    pca = PCA()
    principal_components = pca.fit_transform(df_expanded)
    
    # Get the explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Plot the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio)
    ax.set_title("Explained Variance Ratio of Principal Components")
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    
    # Return the explained variance ratio and the Axes object
    return explained_variance_ratio, ax