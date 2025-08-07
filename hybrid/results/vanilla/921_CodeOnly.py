import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data, columns):
    """
    Normalizes specified columns of a DataFrame using min-max scaling.

    Parameters:
    - data: pandas.DataFrame - The input DataFrame to be normalized.
    - columns: list of str - The list of column names to be normalized.

    Returns:
    - pandas.DataFrame: A new DataFrame with the specified columns normalized between 0 and 1.
    """
    # Create a copy of the DataFrame to avoid modifying the original data
    df_normalized = data.copy()
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the specified columns
    df_normalized[columns] = scaler.fit_transform(df_normalized[columns])
    
    return df_normalized