from sklearn.preprocessing import MinMaxScaler
import numpy as np

def task_func(myList):
    # Convert the list to a numpy array and reshape it for the scaler
    data = np.array(myList).reshape(-1, 1)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Fit the scaler to the data and transform it
    normalized_data = scaler.fit_transform(data)
    
    # Flatten the array to return a 1D array
    return normalized_data.flatten()

# Example usage:
# myList = [10, 20, 30, 40, 50]
# normalized_values = task_func(myList)
# print(normalized_values)