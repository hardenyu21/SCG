import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target_column, target_values=None):
    # Validate inputs
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame.")
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string.")
    if target_values is not None and not hasattr(target_values, '__iter__'):
        raise ValueError("target_values must be an array-like object.")
    
    # Replace elements not in target_values with zeros
    if target_values is not None:
        for column in df.columns:
            if column != target_column:
                df[column] = df[column].apply(lambda x: x if x in target_values else 0)
    
    # Prepare data for linear regression
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Train the Linear Regression model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

# Example usage
rng = np.random.default_rng(seed=0)
df = pd.DataFrame(rng.integers(0, 100, size=(1000, 5)), columns=['A', 'B', 'C', 'D', 'predict'])
model = task_func(df, 'predict', target_values=[10, 20, 30, 40, 50])
print(model.coef_)
print(model.intercept_)