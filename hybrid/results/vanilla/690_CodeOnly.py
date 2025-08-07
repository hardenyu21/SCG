import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

ROWS = 100
COLUMNS = ['X', 'Y']

def task_func(df):
    # Ensure the DataFrame has the correct columns
    if not all(col in df.columns for col in COLUMNS):
        raise ValueError(f"DataFrame must contain columns: {COLUMNS}")
    
    # Prepare the data for linear regression
    X = df[['X']].values  # Features
    y = df['Y'].values    # Target variable
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

# Example usage:
# df = pd.DataFrame(np.random.rand(ROWS, len(COLUMNS)), columns=COLUMNS)
# model = task_func(df)
# print(model.coef_, model.intercept_)