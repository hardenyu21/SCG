import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def task_func(data):
    # Ensure the data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data should be a pandas DataFrame.")
    
    # Check if the required columns are present
    if 'Hours' not in data.columns or 'Scores' not in data.columns:
        raise ValueError("DataFrame must contain 'Hours' and 'Scores' columns.")
    
    # Prepare the data
    X = data[['Hours']].values  # Independent variable
    y = data['Scores'].values   # Dependent variable
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    
    return mse