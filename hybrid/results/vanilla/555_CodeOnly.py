import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def task_func(a, b):
    # Calculate the Pearson correlation coefficient
    correlation_coefficient, _ = stats.pearsonr(a, b)
    
    # Create a Pandas DataFrame from the lists
    df = pd.DataFrame({'A': a, 'B': b})
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['A'], df['B'], label='Data points')
    
    # Calculate the regression line
    slope, intercept, _, _, _ = stats.linregress(df['A'], df['B'])
    regression_line = slope * df['A'] + intercept
    
    # Plot the regression line
    ax.plot(df['A'], regression_line, color='red', label='Regression line')
    
    # Add labels and legend
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.legend()
    
    # Return the correlation coefficient and the Axes object
    return correlation_coefficient, ax

# Example usage:
# a = [1, 2, 3, 4, 5]
# b = [2, 3, 5, 7, 11]
# corr_coeff, ax = task_func(a, b)
# plt.show()