import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(dictionary, key, value, n=100, bins=30, seed=0):
    # Check if the provided value is a number
    if not isinstance(value, (int, float)):
        raise ValueError("The provided value is not a number.")
    
    # Update the dictionary with the specified key-value pair
    dictionary[key] = value
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a random dataset following a normal distribution
    mean = value
    std_dev = value  # Assuming the standard deviation is the same as the mean
    dataset = np.random.normal(loc=mean, scale=std_dev, size=n)
    
    # Convert the dataset to a pandas Series
    dataset_series = pd.Series(dataset)
    
    # Plot the histogram of the generated dataset
    plt.figure(figsize=(8, 6))
    plt.hist(dataset_series, bins=bins, edgecolor='black', alpha=0.7)
    plt.title('Histogram of Generated Dataset')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    
    # Return the updated dictionary and the dataset series
    return dictionary, dataset_series

# Example usage:
# updated_dict, dataset = task_func({'a': 1}, 'b', 2, n=1000)
# print(updated_dict)
# print(dataset)