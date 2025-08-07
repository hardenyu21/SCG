import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(data_matrix):
    # Calculate Z-scores for each row
    z_scores = data_matrix.apply(zscore, axis=1)
    
    # Calculate the mean of Z-scores for each row
    z_scores['Mean'] = z_scores.mean(axis=1)
    
    # Create a correlation matrix of the Z-scores
    corr_matrix = z_scores.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', cbar=True)
    plt.title('Correlation Matrix of Z-scores')
    plt.show()
    
    return z_scores, ax

# Example usage:
# data_matrix = pd.DataFrame({
#     'Feature 1': [1, 2, 3, 4],
#     'Feature 2': [4, 3, 2, 1],
#     'Feature 3': [2, 3, 4, 5]
# })
# z_scores_df, heatmap_ax = task_func(data_matrix)