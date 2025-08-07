import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(my_dict):
    # Check if the value under 'array' key is a numpy array
    if not isinstance(my_dict['array'], np.ndarray):
        raise TypeError("The value of the 'array' key must be a numpy array.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the array to a 2D array if it's 1D, as MinMaxScaler expects 2D input
    array = my_dict['array']
    if array.ndim == 1:
        array = array.reshape(-1, 1)
    
    # Fit and transform the array to normalize it
    normalized_array = scaler.fit_transform(array)
    
    # If the original array was 1D, reshape the normalized array back to 1D
    if my_dict['array'].ndim == 1:
        normalized_array = normalized_array.flatten()
    
    # Add the normalized array to the dictionary
    my_dict['normalized_array'] = normalized_array
    
    # Return the modified dictionary
    return my_dict