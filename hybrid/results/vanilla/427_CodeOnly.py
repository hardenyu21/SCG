import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    # Merge the dataframes on the 'id' column
    merged_df = pd.merge(df1, df2, on='id')
    
    # Prepare the features and target
    X = merged_df[features]
    y = merged_df[target]
    
    # Perform linear regression
    model = LinearRegression()
    model.fit(X, y)
    
    # Get coefficients and intercept
    coefficients = model.coef_.tolist()
    intercept = model.intercept_
    
    # Predict the target values
    y_pred = model.predict(X)
    
    # Calculate residuals
    residuals = y - y_pred
    
    # Plot the residuals
    fig, ax = plt.subplots()
    ax.scatter(y_pred, residuals)
    ax.axhline(y=0, color='r', linestyle='--')
    ax.set_title('Residuals Plot')
    ax.set_xlabel('Predicted Values')
    ax.set_ylabel('Residuals')
    
    # Return the results
    return {
        'coefficients': coefficients,
        'intercept': intercept,
        'residuals_plot': ax
    }