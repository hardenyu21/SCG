import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check for NaN values in the DataFrame
    if df.isnull().values.any():
        raise ValueError("The DataFrame contains NaN values.")
    
    # Check for non-numeric data types
    if not all(np.issubdtype(dtype, np.number) for dtype in df.dtypes):
        raise TypeError("The DataFrame contains non-numeric data types.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Compute the cumulative sum for each column
    cumsum_df = df.cumsum()
    
    # Fit and transform the cumulative sum DataFrame using MinMaxScaler
    normalized_cumsum = scaler.fit_transform(cumsum_df)
    
    # Create a new DataFrame with the normalized cumulative sums
    normalized_cumsum_df = pd.DataFrame(normalized_cumsum, columns=df.columns, index=df.index)
    
    return normalized_cumsum_df