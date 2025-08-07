from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def task_func(L):
    # Flatten the list of lists into a single list of integers
    flat_list = list(chain.from_iterable(L))
    
    # Convert the list to a numpy array and reshape for scikit-learn
    data = np.array(flat_list).reshape(-1, 1)
    
    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data).flatten()
    
    # Plot the standardized values
    fig, ax = plt.subplots()
    ax.plot(standardized_data, marker='o', linestyle='-')
    ax.set_title('Standardized Values')
    ax.set_xlabel('Index')
    ax.set_ylabel('Standardized Value')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ax = task_func(L)