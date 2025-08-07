from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd

def task_func(data, column1, column2):
    # Check if the specified columns exist in the DataFrame
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError("The specified columns do not exist in the DataFrame.")
    
    # Extract the data for the specified columns
    x = data[column1]
    y = data[column2]
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data points')
    ax.plot(x, slope * x + intercept, color='red', label='Fitted line')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.legend()
    
    # Return the regression results and the Axes object
    return (slope, intercept, r_value, p_value, std_err), ax