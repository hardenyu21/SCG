import pandas as pd
import numpy as np

def task_func(df, col):
    """
    Process a Pandas DataFrame by removing a specific column and adding a 'IsEvenIndex' column.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    col (str): The name of the column to be removed.
    
    Returns:
    pd.DataFrame: The processed DataFrame with the specified column removed and a new 'IsEvenIndex' column added.
    """
    # Remove the specified column
    if col in df.columns:
        df = df.drop(columns=[col])
    
    # Add 'IsEvenIndex' column
    df['IsEvenIndex'] = df.index % 2 == 0
    
    return df