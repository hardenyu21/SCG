import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    
    # Check if there are no numeric columns
    if numeric_df.empty:
        raise ValueError("No numeric columns are present.")
    
    # Calculate the cumulative sum of each numeric column
    cumulative_sum_df = numeric_df.cumsum()
    
    # Create a heatmap using Seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(cumulative_sum_df, annot=True, cmap='YlGnBu', fmt='g')
    
    # Return the Axes object
    return ax