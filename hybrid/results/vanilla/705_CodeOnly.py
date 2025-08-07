import numpy as np
from scipy import stats

def task_func(df, column, alpha):
    # Extract the column data as a numpy array
    data = df[column].values
    
    # Perform the Shapiro-Wilk test for normality
    stat, p_value = stats.shapiro(data)
    
    # Determine if the data is normally distributed
    is_normal = p_value > alpha
    
    return is_normal