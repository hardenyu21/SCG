import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(arr):
    # Calculate the sum of each row
    row_sums = np.sum(arr, axis=1)
    
    # Print the sum of each row
    for i, sum_value in enumerate(row_sums):
        print(f"Sum of row {i}: {sum_value}")
    
    # Create a heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(arr, cmap='viridis', vmin=np.min(arr), vmax=np.max(arr))
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# arr = np.random.rand(10, 10)
# ax = task_func(arr)