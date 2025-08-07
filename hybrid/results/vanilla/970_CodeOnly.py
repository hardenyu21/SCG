import numpy as np
import matplotlib.pyplot as plt

def task_func(data: np.ndarray) -> plt.Axes:
    # Check for non-numeric inputs
    if not np.issubdtype(data.dtype, np.number):
        raise TypeError("Input array contains non-numeric inputs.")
    
    # Check for negative numbers or NaNs
    if np.any(data < 0) or np.isnan(data).any():
        raise ValueError("Input array contains negative numbers or NaNs.")
    
    # Sort the data
    sorted_data = np.sort(data)
    
    # Calculate the cumulative probability
    cumulative_prob = np.cumsum(sorted_data) / np.sum(sorted_data)
    
    # Plot the cumulative probability
    fig, ax = plt.subplots()
    ax.plot(range(len(sorted_data)), cumulative_prob, marker='o', linestyle='-')
    ax.set_title("Cumulative Probability Plot")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Probability")
    
    return ax

# Example usage:
# data = np.array([1, 2, 3, 4, 5])
# ax = task_func(data)
# plt.show()