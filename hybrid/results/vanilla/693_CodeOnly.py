import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(tuples_list, columns):
    # Convert the list of tuples into a DataFrame
    df = pd.DataFrame(tuples_list, columns=columns)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a new DataFrame with the scaled data
    df_scaled = pd.DataFrame(scaled_data, columns=columns)
    
    return df_scaled