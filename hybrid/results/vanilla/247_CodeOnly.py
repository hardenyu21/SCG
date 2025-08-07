import pandas as pd
import random
from sklearn.preprocessing import StandardScaler

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    # Validate input
    if max_value < min_value:
        raise ValueError("max_value must be greater than or equal to min_value.")
    
    # Generate random floating point numbers
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_data = [round(num, 3) for num in data]
    
    # Convert to DataFrame
    df = pd.DataFrame(truncated_data, columns=['Original Value'])
    
    # Normalize the data using standard scaling
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(df[['Original Value']])
    
    # Create a new DataFrame with the normalized data
    normalized_df = pd.DataFrame(normalized_data, columns=['Normalized Value'])
    
    return normalized_df

# Example usage
if __name__ == "__main__":
    df = task_func()
    print(df.head())