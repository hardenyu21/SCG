import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(P, T):
    # Check if the shapes of P and T are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("The number of columns in P must match the first dimension of T.")
    
    # Perform matrix-tensor multiplication
    # P is of shape (m, n) and T is of shape (n, p, q)
    # The result will be a 3D array of shape (m, p, q)
    result = np.tensordot(P, T, axes=(1, 0))
    
    # Flatten the result to a 2D array
    # The new shape will be (m, p*q)
    flattened_result = result.reshape(result.shape[0], -1)
    
    # Normalize the flattened result using StandardScaler
    scaler = StandardScaler()
    normalized_result = scaler.fit_transform(flattened_result)
    
    # Create column names for the DataFrame
    num_features = normalized_result.shape[1]
    column_names = [f'feature_{i}' for i in range(num_features)]
    
    # Create and return the DataFrame
    return pd.DataFrame(normalized_result, columns=column_names)