import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_lists, seed=42):
    # Set the random seed for reproducibility
    random.seed(seed)
    np.random.seed(seed)
    
    # Fill empty inner lists with five random integers between 0 and 100
    for i in range(len(list_of_lists)):
        if not list_of_lists[i]:
            list_of_lists[i] = [random.randint(0, 100) for _ in range(5)]
    
    # Flatten the list of lists to scale all values together
    flat_list = [item for sublist in list_of_lists for item in sublist]
    
    # Reshape the flat list to a 2D array for MinMaxScaler
    flat_list_reshaped = np.array(flat_list).reshape(-1, 1)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Fit and transform the data
    scaled_flat_list = scaler.fit_transform(flat_list_reshaped)
    
    # Reshape the scaled data back into the original list of lists structure
    scaled_list_of_lists = []
    index = 0
    for sublist in list_of_lists:
        sublist_length = len(sublist)
        scaled_sublist = scaled_flat_list[index:index + sublist_length].flatten().tolist()
        scaled_list_of_lists.append(scaled_sublist)
        index += sublist_length
    
    return scaled_list_of_lists