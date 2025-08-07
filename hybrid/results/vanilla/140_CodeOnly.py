import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, cols):
    # Check if 'df' is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if 'cols' is a list
    if not isinstance(cols, list):
        raise ValueError("Input 'cols' must be a list.")
    
    # Check if all columns in 'cols' exist in 'df'
    missing_cols = [col for col in cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Columns {missing_cols} do not exist in the DataFrame.")
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the specified columns
    df[cols] = scaler.fit_transform(df[cols])
    
    return df