import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def task_func(data_matrix):
    # Calculate the skewness for each row
    skewness_values = data_matrix.apply(lambda row: skew(row), axis=1)
    
    # Create a DataFrame to store the skewness values
    skewness_df = pd.DataFrame({'Skewness': skewness_values})
    
    # Plot the distribution of skewness values
    fig, ax = plt.subplots()
    skewness_df['Skewness'].plot(kind='hist', bins=30, ax=ax)
    ax.set_title('Distribution of Row Skewness')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')
    
    # Return the DataFrame and the Axes object
    return skewness_df, ax

# Example usage:
# data_matrix = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [5, 4, 3, 2, 1],
#     'C': [2, 3, 4, 5, 6]
# })
# skewness_df, ax = task_func(data_matrix)
# plt.show()