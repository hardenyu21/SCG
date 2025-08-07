import pandas as pd
from statsmodels.tsa.stattools import adfuller

def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df[column_b] > 50) & (df[column_c] == 900)]
    
    # Extract the relevant column after filtering
    filtered_column_a = filtered_df[column_a]
    
    # Check if column_a is empty or has constant values
    if filtered_column_a.empty or filtered_column_a.nunique() == 1:
        return True
    
    # Perform the Augmented Dickey-Fuller test
    adf_result = adfuller(filtered_column_a)
    p_value = adf_result[1]
    
    # Determine if the data is stationary
    return p_value < 0.05