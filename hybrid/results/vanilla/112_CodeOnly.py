import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a pandas DataFrame and contains the 'Status' column
    if not isinstance(df, pd.DataFrame) or 'Status' not in df.columns:
        raise ValueError("Input must be a pandas DataFrame with a 'Status' column.")
    
    # Count the occurrences of each status
    status_counts = df['Status'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Return the Axes object
    return ax