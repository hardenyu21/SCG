import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the DataFrame has the required columns
    if 'Date' not in df.columns or 'Value' not in df.columns:
        raise KeyError("The DataFrame must contain 'Date' and 'Value' columns.")
    
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Split 'Value' lists into separate columns
    value_df = df['Value'].apply(pd.Series)
    
    # Calculate Z-scores for each column in the value_df
    zscore_df = value_df.apply(zscore, axis=0)
    
    # Replace the original 'Value' column with the Z-scores
    df = df.drop(columns=['Value']).join(zscore_df)
    
    # Create a box plot for Z-scores over time
    fig, ax = plt.subplots(figsize=(10, 6))
    df.set_index('Date').boxplot(ax=ax)
    ax.set_title("Z-Scores Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Z-Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return df, fig