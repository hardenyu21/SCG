import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    # Convert the data dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Remove the specified column if it exists
    if column in df.columns:
        df = df.drop(columns=[column])
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include='number')
    
    # Check if there are any numeric columns left
    if numeric_df.empty:
        return None
    
    # Calculate the correlation matrix
    corr_matrix = numeric_df.corr()
    
    # Create a heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    
    # Return the Axes object
    return ax