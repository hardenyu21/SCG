import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    # Check if the array is empty or not 2-dimensional
    if array.size == 0 or array.ndim != 2:
        raise ValueError("The array must be non-empty and 2-dimensional.")
    
    # Check if features is provided and matches the number of columns
    if features is not None and len(features) != array.shape[1]:
        raise ValueError("The number of features must match the number of columns in the array.")
    
    # Set the random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Shuffle the columns of the array
    shuffled_indices = np.random.permutation(array.shape[1])
    shuffled_array = array[:, shuffled_indices]
    
    # Prepare the feature labels
    if features is None:
        features = [str(i + 1) for i in range(array.shape[1])]
    else:
        features = [features[i] for i in shuffled_indices]
    
    # Create the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(shuffled_array, xticklabels=features, yticklabels=False, cmap='viridis')
    plt.xlabel('Features')
    plt.title('Shuffled Column Heatmap')
    plt.show()
    
    return ax