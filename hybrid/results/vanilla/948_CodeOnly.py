import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(rows=3, columns=2, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a matrix of random values
    random_matrix = np.random.rand(rows, columns)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Reshape the matrix to fit the scaler's input requirements
    reshaped_matrix = random_matrix.reshape(-1, 1)
    
    # Scale the matrix
    scaled_matrix = scaler.fit_transform(reshaped_matrix)
    
    # Reshape back to the original matrix dimensions
    scaled_matrix = scaled_matrix.reshape(rows, columns)
    
    return scaled_matrix

# Example usage
print(task_func(2, 2))