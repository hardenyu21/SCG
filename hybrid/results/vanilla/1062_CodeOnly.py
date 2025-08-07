import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def task_func(arr):
    # Check if the array is empty
    if arr.size == 0:
        # Create an empty plot
        fig, ax = plt.subplots()
        ax.set_title('Time Series of Row Sums')
        plt.show()
        return ax
    
    # Calculate the sum of each row
    row_sums = np.sum(arr, axis=1)
    
    # Create a date range starting from January 1, 2020
    start_date = '2020-01-01'
    dates = pd.date_range(start=start_date, periods=len(row_sums))
    
    # Create a DataFrame with the row sums and dates
    df = pd.DataFrame({'Date': dates, 'Row Sum': row_sums})
    
    # Plot the time series
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Row Sum'], marker='o')
    ax.set_title('Time Series of Row Sums')
    ax.set_xlabel('Date')
    ax.set_ylabel('Row Sum')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return ax