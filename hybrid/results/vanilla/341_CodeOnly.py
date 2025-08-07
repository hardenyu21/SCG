import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, col):
    # Validate input
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df must be a pandas DataFrame.")
    if df.empty:
        raise ValueError("The input DataFrame must not be empty.")
    if col not in df.columns:
        raise ValueError(f"The specified column '{col}' is not in the DataFrame.")
    
    # Create a matplotlib figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot histogram with kernel density estimate
    sns.histplot(df[col], kde=True, ax=axes[0])
    axes[0].set_title(f'Histogram of {col}')
    axes[0].set_xlabel(col)
    axes[0].set_ylabel('Frequency')
    
    # Plot box plot
    sns.boxplot(y=df[col], ax=axes[1])
    axes[1].set_title(f'Box Plot of {col}')
    axes[1].set_ylabel(col)
    
    # Adjust layout
    plt.tight_layout()
    
    # Return the figure object
    return fig