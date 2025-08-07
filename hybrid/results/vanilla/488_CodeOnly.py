from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_time, end_time, step, amplitude, period, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Convert start and end times to datetime objects
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    
    # Generate timestamps
    timestamps = []
    current_time = start_time
    while current_time <= end_time:
        timestamps.append(current_time)
        current_time += timedelta(seconds=step)
    
    # Create a DataFrame with timestamps
    df = pd.DataFrame(timestamps, columns=['Timestamp'])
    
    # Generate seasonality component
    df['Seasonality'] = amplitude * np.sin(2 * np.pi * (df.index / period))
    
    # Generate random noise
    df['Noise'] = np.random.normal(0, 1, len(df))
    
    # Combine seasonality and noise to create the time series
    df['Value'] = df['Seasonality'] + df['Noise']
    
    # Plot the time series
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Timestamp'], df['Value'], label='Time Series with Seasonality')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Value')
    ax.set_title('Time Series with Seasonality')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return ax

# Example usage:
# ax = task_func('2023-01-01 00:00:00', '2023-01-02 00:00:00', 3600, 10, 24)
# plt.show()