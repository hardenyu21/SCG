import pandas as pd
import numpy as np
import statsmodels.api as sm

def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    # Validate input list
    if not isinstance(array, list) or not all(isinstance(row, list) for row in array):
        raise ValueError("Input must be a 2D list.")
    
    if not all(len(row) == 5 for row in array):
        raise ValueError("Each row in the list must have exactly 5 elements.")
    
    # Create DataFrame
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'Response'])
    
    # Separate independent and dependent variables
    X = df[['A', 'B', 'C', 'D']]
    y = df['Response']
    
    # Add a constant to the model
    X = sm.add_constant(X)
    
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    
    # Fit the linear regression model
    model = sm.OLS(y, X)
    results = model.fit()
    
    return df, results

# Example usage:
# array = [
#     [1, 2, 3, 4, 10],
#     [2, 3, 4, 5, 15],
#     [3, 4, 5, 6, 20],
#     [4, 5, 6, 7, 25]
# ]
# df, results = task_func(array)
# print(df)
# print(results.summary())