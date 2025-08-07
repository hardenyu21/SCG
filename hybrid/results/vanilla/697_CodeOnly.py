import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Extract the feature and target columns
    X = df[['feature']].values  # Assuming 'feature' is the column name for the independent variable
    y = df['value'].values      # Assuming 'value' is the column name for the dependent variable

    # Initialize the Linear Regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y)

    # Get the coefficients and intercept
    coefficients = model.coef_
    intercept = model.intercept_

    # Create a result dictionary
    result = {
        'coefficients': coefficients[0],  # Since we have only one feature, we take the first element
        'intercept': intercept
    }

    return result