import pandas as pd
from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt

def task_func(start_date, end_date, num_series, seed=None):
    # Validate input parameters
    if start_date > end_date:
        raise ValueError("start_date must be earlier than end_date.")
    if num_series < 1:
        raise ValueError("num_series must be at least 1.")
    
    # Set random seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Generate date range
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Generate random time series data
    data = {}
    for i in range(num_series):
        series_name = f'series_{i+1}'
        data[series_name] = [random.randint(0, 100) for _ in date_range]
    
    # Create DataFrame
    df = pd.DataFrame(data, index=date_range)
    
    # Plot the time series
    ax = df.plot(title="Random Time Series", figsize=(10, 6))
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    plt.legend(title="Series")
    plt.grid(True)
    plt.tight_layout()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# df, ax = task_func(datetime(2023, 1, 1), datetime(2023, 1, 10), 3, seed=42)
# plt.show()