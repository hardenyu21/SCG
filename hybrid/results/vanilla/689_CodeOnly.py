import numpy as np
import pandas as pd
from scipy import stats

def task_func(df):
    """
    Perform the Shapiro-Wilk test for normality on each column of the DataFrame.

    Parameters:
    df (pd.DataFrame): A DataFrame with numeric values.

    Returns:
    dict: A dictionary with column names as keys and p-values from the Shapiro-Wilk test as values.
    """
    results = {}
    for column in df.columns:
        # Perform the Shapiro-Wilk test
        stat, p_value = stats.shapiro(df[column])
        # Store the p-value in the results dictionary
        results[column] = p_value
    return results

# Example usage:
# df = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])
# p_values = task_func(df)
# print(p_values)