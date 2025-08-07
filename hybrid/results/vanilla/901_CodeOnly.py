import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Updated function to handle empty input list
def task_func(d):
    if not d:
        return pd.DataFrame()

    # Extract the values for scaling
    data = [[item['x'], item['y'], item['z']] for item in d]
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a new DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=['x', 'y', 'z'])
    
    return scaled_df

# Example usage
data = [{'x': -1, 'y': 0, 'z': 5}, {'x': 3, 'y': -15, 'z': 0}, {'x': 0, 'y': 1, 'z': -7}]
print(task_func(data))