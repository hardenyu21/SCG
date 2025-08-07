import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    # Generate normally distributed data
    normal_data = np.random.normal(loc=0, scale=1, size=num_samples)
    
    # Introduce artificial outliers
    outliers = np.random.uniform(low=-10, high=10, size=num_outliers)
    
    # Combine normal data and outliers
    data = np.concatenate((normal_data, outliers))
    
    # Sort data to facilitate IQR calculation
    sorted_data = np.sort(normal_data)
    
    # Calculate Q1 and Q3
    Q1 = np.percentile(sorted_data, 25)
    Q3 = np.percentile(sorted_data, 75)
    
    # Calculate IQR
    IQR = Q3 - Q1
    
    # Define outlier boundaries
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Detect outliers in the normally distributed data
    outliers_detected = normal_data[(normal_data < lower_bound) | (normal_data > upper_bound)]
    
    # Plot histogram of the combined data
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, alpha=0.7, color='blue', edgecolor='black')
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Highlight detected outliers
    ax.scatter(outliers_detected, np.zeros_like(outliers_detected) - 0.1, color='red', zorder=5, label='Detected Outliers')
    ax.scatter(outliers, np.zeros_like(outliers) - 0.2, color='green', zorder=5, label='Artificial Outliers')
    ax.legend()
    
    # Show plot
    plt.show()
    
    return data, outliers_detected, ax

# Example usage
data, outliers_detected, ax = task_func()