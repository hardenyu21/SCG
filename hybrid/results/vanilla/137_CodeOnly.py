import pandas as pd
from scipy.stats import skew

def task_func(df):
    # Check if the input is a DataFrame and has at least one column
    if not isinstance(df, pd.DataFrame) or df.shape[1] == 0:
        raise ValueError("If the input is not a DataFrame or has no columns.")
    
    # Calculate the skewness of the last column
    last_column_skewness = skew(df.iloc[:, -1])
    
    return last_column_skewness