import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Apply PCA
    pca = PCA(n_components=n_components)
    pca.fit(data_matrix)
    
    # Transform the data
    transformed_data = pca.transform(data_matrix)
    
    # Create a DataFrame with the transformed data
    columns = [f'Component {i+1}' for i in range(n_components)]
    df = pd.DataFrame(transformed_data, columns=columns)
    
    # Calculate the mean of each component for each row
    df['Mean'] = df.mean(axis=1)
    
    # Calculate cumulative explained variance
    cumulative_explained_variance = pca.explained_variance_ratio_.cumsum()
    
    # Plot the cumulative explained variance
    fig, ax = plt.subplots()
    ax.plot(range(1, n_components + 1), cumulative_explained_variance, marker='o')
    ax.set_xlabel('Number of Components')
    ax.set_ylabel('Cumulative Explained Variance')
    ax.set_title('Cumulative Explained Variance by Number of Components')
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# data_matrix = [[1, 2], [3, 4], [5, 6]]
# df, ax = task_func(data_matrix, n_components=2)
# plt.show()