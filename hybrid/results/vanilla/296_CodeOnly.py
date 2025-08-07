import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Count the occurrences of each unique value in the 'value' column
    value_counts = df['value'].value_counts()
    
    # Create a bar chart
    fig, ax = plt.subplots()
    value_counts.plot(kind='bar', ax=ax)
    
    # Set the title and labels
    ax.set_title("Value Distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    
    # Return the Axes object
    return ax