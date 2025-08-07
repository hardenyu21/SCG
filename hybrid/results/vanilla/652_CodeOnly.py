import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Constants
TARGET_VALUE = '332'
ARRAY = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])

def task_func(target_value=TARGET_VALUE, array=ARRAY):
    # Find row indices where the first cell matches the target value
    indices = [i for i, row in enumerate(array) if row[0] == target_value]
    
    # Check if any indices were found
    if not indices:
        return 'N/A'
    
    # Perform statistical analysis
    mean = np.mean(indices)
    variance = np.var(indices)
    skewness = stats.skew(indices)
    kurtosis = stats.kurtosis(indices)
    
    # Plot the distribution of indices
    plt.hist(indices, bins=len(indices), edgecolor='black')
    plt.title('Distribution of Indices')
    plt.xlabel('Index')
    plt.ylabel('Frequency')
    plt.show()
    
    return (mean, variance, skewness, kurtosis)

# Example usage
result = task_func()
print(result)