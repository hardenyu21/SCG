import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(array):
    # Check if the input array is empty
    if not array:
        raise ValueError("The input array is empty.")
    
    # Check if all sublists have the same length (5)
    if not all(len(sublist) == 5 for sublist in array):
        raise ValueError("The input array contains sublists of varying lengths.")
    
    # Define column names
    columns = ['A', 'B', 'C', 'D', 'E']
    
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(array, columns=columns)
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(8, 6))
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df, heatmap

# Example usage:
# array = [
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [2, 3, 4, 5, 6],
#     [6, 5, 4, 3, 2]
# ]
# df, heatmap = task_func(array)