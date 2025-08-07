from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(l):
    # Convert the input list to a numpy array and reshape it for scaling
    data = np.array(l).reshape(-1, 1)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(data)
    
    # Create a DataFrame with the scaled values
    df = pd.DataFrame(scaled_data, columns=['Scaled Values'])
    
    return df