import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

def task_func(original):
    # Convert the original list to a numpy array
    original_array = np.array(original)
    
    # Normalize the array using Min-Max scaling
    min_max_scaler = preprocessing.MinMaxScaler()
    normalized_array = min_max_scaler.fit_transform(original_array.reshape(-1, 1)).flatten()
    
    # Plot the original and normalized arrays
    fig, ax = plt.subplots()
    ax.plot(original_array, label='Original', marker='o')
    ax.plot(normalized_array, label='Normalized', marker='x')
    ax.set_title('Original vs. Normalized Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the original array, normalized array, and Axes object
    return original_array, normalized_array, ax

# Example usage:
# original_data = [10, 20, 30, 40, 50]
# original_array, normalized_array, ax = task_func(original_data)