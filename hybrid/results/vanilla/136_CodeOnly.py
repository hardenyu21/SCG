import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame and if it is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)
    
    # Create a DataFrame with the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])
    
    # Plot the principal components
    fig, ax = plt.subplots()
    ax.scatter(principal_df['Principal Component 1'], principal_df['Principal Component 2'])
    ax.set_title('2 Component PCA')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    
    # Return the DataFrame and the Axes object
    return principal_df, ax