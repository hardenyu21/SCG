import seaborn as sns
import numpy as np
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the DataFrame contains non-numeric data types
    if not all(np.issubdtype(dtype, np.number) for dtype in df.dtypes):
        raise TypeError("The DataFrame contains non-numeric data types.")
    
    # Calculate the covariance matrix
    covariance_df = df.cov()
    
    # Generate the pair plot
    pair_plot = sns.pairplot(df)
    
    return covariance_df, pair_plot