import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(df: pd.DataFrame) -> tuple:
    # Create a figure with two subplots: one for the box plot and one for the histogram
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Box plot
    sns.boxplot(y=df['Close'], ax=axes[0])
    axes[0].set_title('Box Plot of Closing Prices')
    axes[0].set_ylabel('Closing Price')

    # Histogram
    sns.histplot(df['Close'], bins=30, kde=True, ax=axes[1])
    axes[1].set_title('Histogram of Closing Prices')
    axes[1].set_xlabel('Closing Price')
    axes[1].set_ylabel('Frequency')

    # Adjust layout
    plt.tight_layout()

    # Return the axes objects
    return axes