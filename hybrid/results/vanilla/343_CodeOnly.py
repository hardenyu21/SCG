import pandas as pd
import matplotlib.pyplot as plt

# Constants for pie chart colors
COLORS = ['r', 'g', 'b', 'y', 'm']

def task_func(df, col, title=None):
    # Validate input
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df must be a DataFrame.")
    if df.empty:
        raise ValueError("The DataFrame must not be empty.")
    if col not in df.columns:
        raise ValueError(f"The DataFrame must contain the column '{col}'.")
    
    # Count unique values in the specified column
    value_counts = df[col].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(value_counts, labels=value_counts.index, colors=COLORS[:len(value_counts)], autopct='%1.1f%%', startangle=90)
    
    # Set the title if provided
    if title:
        ax.set_title(title)
    
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')
    
    # Return the Axes object
    return ax