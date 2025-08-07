import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Calculate the correlation matrix
    corr_matrix = data.corr()
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    
    # Set the title of the heatmap
    ax.set_title('Correlation Matrix')
    
    # Return the Axes object
    return ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [5, 4, 3, 2, 1],
#     'C': [2, 3, 4, 5, 6]
# })
# ax = task_func(df)
# plt.show()