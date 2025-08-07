import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Fill missing values with the column's average
    numeric_df_filled = numeric_df.fillna(numeric_df.mean())
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(numeric_df_filled)
    
    # Create a DataFrame with the first two principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['Component 1', 'Component 2'])
    
    # Plot the scatter plot
    plt.figure(figsize=(8, 6))
    ax = sns.scatterplot(x='Component 1', y='Component 2', data=principal_df)
    ax.set_xlabel('Component 1')
    ax.set_ylabel('Component 2')
    plt.title('PCA of Dataset')
    
    # Return the DataFrame and the Axes object
    return principal_df, ax

# Example usage:
# df = pd.read_csv('your_dataset.csv')
# principal_df, ax = task_func(df)
# plt.show()