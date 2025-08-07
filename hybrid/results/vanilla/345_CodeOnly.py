import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, col1, col2):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the specified columns exist in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"The DataFrame does not contain the specified columns: {col1} and/or {col2}.")
    
    # Check if the specified columns contain numeric data
    if not pd.api.types.is_numeric_dtype(df[col1]) or not pd.api.types.is_numeric_dtype(df[col2]):
        raise TypeError(f"The specified columns {col1} and/or {col2} contain non-numeric data.")
    
    # Create a scatter plot with a regression line
    ax = sns.lmplot(x=col1, y=col2, data=df, aspect=1.5, height=6)
    
    # Return the seaborn axes object
    return ax.axes[0, 0]

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [2, 3, 5, 7, 11]
# })
# ax = task_func(df, 'A', 'B')
# plt.show()