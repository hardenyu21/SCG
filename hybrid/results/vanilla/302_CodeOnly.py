import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
COLUMNS = ['Date', 'Value']

def task_func(df, plot=False):
    # Validate input DataFrame
    if df.empty:
        raise ValueError("The input DataFrame is empty.")
    
    if 'Value' not in df.columns:
        raise ValueError("The DataFrame does not contain a 'Value' column.")
    
    # Ensure 'Value' column contains lists
    if not all(isinstance(item, list) for item in df['Value']):
        raise ValueError("The 'Value' column must contain lists.")
    
    # Split lists in 'Value' column into separate columns
    value_df = pd.DataFrame(df['Value'].tolist(), index=df.index)
    
    # Calculate the Pearson correlation coefficient matrix
    correlation_matrix = value_df.corr(method='pearson')
    
    # Plot the correlation matrix as a heatmap if requested
    ax = None
    if plot:
        plt.figure(figsize=(10, 8))
        ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True)
        plt.title("Correlation Heatmap")
        plt.show()
    
    return correlation_matrix, ax