import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    standardized_data = scaler.fit_transform(df)
    
    # Create a new DataFrame with the standardized data
    df_standardized = pd.DataFrame(standardized_data, columns=df.columns, index=df.index)
    
    return df_standardized