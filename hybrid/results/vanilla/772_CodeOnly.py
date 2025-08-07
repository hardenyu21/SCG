import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def task_func(num_samples=1000, k=5, d=2, random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random numbers from a Gaussian normal distribution
    original_data = np.random.randn(num_samples, 1)
    
    # Apply a linear transformation: y = kx + d
    transformed_data = k * original_data + d
    
    # Standardize the transformed data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(transformed_data)
    
    # Calculate the mean squared error between the original and standardized data
    mse = mean_squared_error(original_data, standardized_data)
    
    return mse

# Example usage
mse = task_func()
print(mse)  # Output will vary depending on the random seed and parameters

mse = task_func(k=1, d=0)
print(mse)  # Output will vary depending on the random seed and parameters