import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Drop rows with duplicate names
    df_unique = df.drop_duplicates(subset='name')
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(df_unique['age'], df_unique['score'])
    
    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df_unique['age'], df_unique['score'], label='Data points')
    
    # Plot the regression line
    regression_line = slope * df_unique['age'] + intercept
    ax.plot(df_unique['age'], regression_line, color='red', label='Regression line')
    
    # Set the title and labels
    ax.set_title('Linear Regression')
    ax.set_xlabel('Age')
    ax.set_ylabel('Score')
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the plot and axes objects
    return plt, ax