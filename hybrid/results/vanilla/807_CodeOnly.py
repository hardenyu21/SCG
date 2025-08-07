import numpy as np
from scipy.stats import norm

def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    # Calculate the mean and standard deviation of the data
    mean = np.mean(data)
    std_dev = np.std(data)
    
    # Calculate the variance
    var = std_dev ** 2
    
    # If the standard deviation is 0, return an empty list for outliers
    if std_dev == 0:
        return [], mean, var
    
    # Calculate the Z scores for each data point
    z_scores = (data - mean) / std_dev
    
    # Find the indices of outliers where the absolute Z score is greater than the threshold
    outliers = [index for index, z_score in enumerate(z_scores) if abs(z_score) > threshold]
    
    return outliers, mean, var

# Example usage
data = np.array([-10, 3, 5, 5, 5, 5, 5, 7, 20])
outliers, mean, var = task_func(data, threshold=4)
print(outliers)  # Output: []
print(mean)       # Output: 5.0
print(var)        # Output: 50.888888888888886