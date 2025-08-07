import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
FEATURE_NAMES = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]

def task_func(data_matrix):
    # Standardize the data matrix
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_matrix)
    
    # Create a DataFrame with the standardized data
    df = pd.DataFrame(standardized_data, columns=FEATURE_NAMES)
    
    # Calculate the mean of each row
    df['Mean'] = df.mean(axis=1)
    
    # Plot the distribution of the mean values
    fig, ax = plt.subplots()
    ax.hist(df['Mean'], bins=10, edgecolor='black')
    ax.set_title('Distribution of Means')
    ax.set_xlabel('Mean Value')
    ax.set_ylabel('Frequency')
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# data_matrix = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6]]
# df, ax = task_func(data_matrix)
# plt.show()