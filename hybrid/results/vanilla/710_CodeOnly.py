import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_path):
    # Load the dataset from the CSV file
    df = pd.read_csv(data_path)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data using the scaler
    # Assuming all columns need to be normalized
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)
    
    return df_normalized