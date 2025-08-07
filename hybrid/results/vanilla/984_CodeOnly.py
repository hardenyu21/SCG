import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

def task_func(df, x_column, y_column):
    # Extract the specified columns from the DataFrame
    X = df[[x_column]].values
    y = df[y_column].values
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(X, y, color='blue', label='Data points')
    
    # Fit a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict using the model
    y_pred = model.predict(X)
    
    # Plot the regression line
    ax.plot(X, y_pred, color='red', label='Regression line')
    
    # Add labels and legend
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax