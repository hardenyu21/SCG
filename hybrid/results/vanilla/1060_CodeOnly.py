import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame, column_name: str) -> (str, plt.Axes):
    # Check if the DataFrame is empty or the column does not exist
    if df.empty or column_name not in df.columns:
        fig, ax = plt.subplots()
        ax.set_title(f"Distribution of values in {column_name} (No Data)")
        return "The DataFrame is empty or the specified column has no data.", ax
    
    # Check if the column contains only null values
    if df[column_name].isnull().all():
        fig, ax = plt.subplots()
        ax.set_title(f"Distribution of values in {column_name} (No Data)")
        return "The DataFrame is empty or the specified column has no data.", ax
    
    # Get the value counts
    value_counts = df[column_name].value_counts()
    
    # Calculate if the distribution is uniform
    if len(value_counts) == 1:
        is_uniform = True
    else:
        max_count = value_counts.max()
        min_count = value_counts.min()
        is_uniform = max_count == min_count
    
    # Generate the histogram
    fig, ax = plt.subplots()
    value_counts.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black', alpha=0.7)
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Distribution of values in {column_name}")
    
    # Return the appropriate message and the Axes object
    if is_uniform:
        return "The distribution of values is uniform.", ax
    else:
        return "The distribution of values is not uniform.", ax