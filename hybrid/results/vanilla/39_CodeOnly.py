import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

# Constants
ALPHA = 0.05

def task_func(data_matrix):
    # Calculate the mean of each row
    row_means = np.mean(data_matrix, axis=1)
    
    # Calculate the population mean
    population_mean = np.mean(data_matrix)
    
    # Initialize a list to store indices of significant means
    significant_indices = []
    
    # Perform t-test for each row mean against the population mean
    for i, row_mean in enumerate(row_means):
        t_stat, p_value = ttest_1samp(data_matrix[i], population_mean)
        if p_value < ALPHA:
            significant_indices.append(i)
    
    # Plotting
    fig, ax = plt.subplots()
    
    # Plot the mean of each row
    ax.plot(range(len(row_means)), row_means, color='red', label='Means')
    
    # Plot the significant means
    if significant_indices:
        ax.plot(significant_indices, row_means[significant_indices], 'bo', label='Significant Means')
    
    # Plot the population mean as a horizontal line
    ax.axhline(y=population_mean, color='green', linestyle='--', label='Population Mean')
    
    # Add labels and legend
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Mean Value')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return significant_indices, ax

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices, ax = task_func(data)
print(indices)