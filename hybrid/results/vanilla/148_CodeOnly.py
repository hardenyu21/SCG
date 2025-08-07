import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()
    
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Fit and transform the column with LabelEncoder
    df[column_name] = label_encoder.fit_transform(df[column_name])
    
    # Return the DataFrame with the encoded column
    return df