import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Constants
ARRAY_LENGTH = 10

def task_func():
    # Generate a random array
    random_array = np.random.rand(ARRAY_LENGTH)
    
    # Reshape the array to fit the scaler's input requirements
    random_array_reshaped = random_array.reshape(-1, 1)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Fit and transform the array
    scaled_array_reshaped = scaler.fit_transform(random_array_reshaped)
    
    # Reshape back to the original array shape
    scaled_array = scaled_array_reshaped.flatten()
    
    return scaled_array

# Example usage
scaled_array = task_func()
print(scaled_array)