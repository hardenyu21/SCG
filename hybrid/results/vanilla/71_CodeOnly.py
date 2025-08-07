import pandas as pd
import seaborn as sns
import numpy as np
import ast
import matplotlib.pyplot as plt

def task_func(csv_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Ensure the 'list' column is converted from string to list
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate sum, mean, and standard deviation for each list
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['std'] = df['list'].apply(np.std)
    
    # Plot a histogram of the mean values
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(df['mean'], bins=10, kde=True)
    plt.title('Histogram of Mean Values')
    plt.xlabel('Mean')
    plt.ylabel('Frequency')
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# df, ax = task_func('emails.csv')
# plt.show()