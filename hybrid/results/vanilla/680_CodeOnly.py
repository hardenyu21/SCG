import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(df, features):
    """
    Standardizes the specified features in the DataFrame using StandardScaler.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    features (list): A list of column names to be standardized.

    Returns:
    pandas.DataFrame: The DataFrame with the standardized features.
    """
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the specified features
    df[features] = scaler.fit_transform(df[features])
    
    return df