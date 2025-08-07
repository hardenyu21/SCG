import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, kstest

def task_func(data_dict):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)
    
    # List to store the Axes objects
    axes_list = []
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Create a histogram for the column
        fig, ax = plt.subplots()
        df[column].hist(ax=ax, bins=10, edgecolor='black')
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        
        # Append the Axes object to the list
        axes_list.append(ax)
        
        # Check if the distribution is uniform
        # Perform a Kolmogorov-Smirnov test against a uniform distribution
        _, p_value = kstest(df[column], uniform(loc=df[column].min(), scale=df[column].max()).cdf)
        
        # Print a message if the distribution is not uniform
        if p_value < 0.05:
            print(f"The distribution of {column} is not uniform (p-value: {p_value:.4f}).")
    
    # Return the list of Axes objects
    return axes_list