from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_time, end_time, step, trend, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Convert start and end times to datetime objects
    start_time = datetime.fromtimestamp(start_time)
    end_time = datetime.fromtimestamp(end_time)
    
    # Generate timestamps
    timestamps = []
    current_time = start_time
    while current_time <= end_time:
        timestamps.append(current_time)
        current_time += timedelta(seconds=step)
    
    # Generate values from a normal distribution and add a linear trend
    num_points = len(timestamps)
    values = np.random.normal(loc=0, scale=1, size=num_points) + np.linspace(0, trend * num_points, num_points)
    
    # Create a DataFrame
    df = pd.DataFrame({'Time': timestamps, 'Value': values})
    
    # Plot the time series
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Value'], marker='o')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Time Series with Trend')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func(1609459200, 1609545600, 3600, 0.1)
# plt.show()