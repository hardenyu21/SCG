import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

def task_func(data, column, outlier_z_score):
    """
    Identifies and removes outliers from a specified column of a dataset based on the Z-score.
    
    Parameters:
    - data: A pandas DataFrame containing the dataset.
    - column: The name of the column from which to remove outliers.
    - outlier_z_score: The Z-score threshold above which data points are considered outliers.
    
    Returns:
    - A tuple containing the original data, the data without outliers, and the indices of the outliers.
    """
    # Extract the specified column
    column_data = data[column].values.reshape(-1, 1)
    
    # Standardize the column
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(column_data)
    
    # Calculate Z-scores
    z_scores = np.abs(stats.zscore(standardized_data))
    
    # Identify outliers
    outliers = np.where(z_scores > outlier_z_score)[0]
    
    # Remove outliers
    data_without_outliers = data.drop(index=outliers)
    
    # Plotting
    plt.figure(figsize=(12, 6))
    
    # Plot data with outliers
    plt.subplot(1, 2, 1)
    plt.scatter(range(len(data)), data[column], color='blue', label='Data Points')
    plt.scatter(outliers, data.iloc[outliers][column], color='red', label='Outliers')
    plt.title('Data with Outliers')
    plt.xlabel('Index')
    plt.ylabel(column)
    plt.legend()
    
    # Plot data without outliers
    plt.subplot(1, 2, 2)
    plt.scatter(range(len(data_without_outliers)), data_without_outliers[column], color='green', label='Data Points')
    plt.title('Data without Outliers')
    plt.xlabel('Index')
    plt.ylabel(column)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    return data, data_without_outliers, outliers

# Example usage:
# df = pd.DataFrame({'A': [1, 2, 3, 4, 100, 6, 7, 8, 9]})
# original_data, data_without_outliers, outliers = task_func(df, 'A', 2)