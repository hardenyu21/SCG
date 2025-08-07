import numpy as np
import pandas as pd
from scipy.stats import linregress

def task_func(df, x_col, y_col):
    """
    Perform linear regression on two variables in a DataFrame and add a 'predicted' column.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data.
    x_col (str): The name of the column to be used as the independent variable.
    y_col (str): The name of the column to be used as the dependent variable.

    Returns:
    pandas.DataFrame: The DataFrame with the added 'predicted' column.
    """
    # Extract the data for the two variables
    x = df[x_col]
    y = df[y_col]
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Calculate the predicted values
    df['predicted'] = slope * x + intercept
    
    return df

# Example usage:
# df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 4, 5]})
# df = task_func(df, 'x', 'y')
# print(df)