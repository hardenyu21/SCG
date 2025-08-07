import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def task_func(data, target_column, test_size=0.2, random_state=0) -> float:
    # Validate input data
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data is not a DataFrame.")
    if data.empty:
        raise ValueError("data is empty.")
    if target_column not in data.columns:
        raise ValueError("target_column is not a column of data.")
    if not np.issubdtype(data.dtypes, np.number).all():
        raise ValueError("data contains values that are not numeric.")
    if not isinstance(random_state, int):
        raise ValueError("random_state is not an integer.")
    if not (0 < test_size < 1):
        raise ValueError("test_size is not between 0 and 1.")
    
    # Split the data into features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Return the model's score on the test set
    return model.score(X_test, y_test)