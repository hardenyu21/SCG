import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a date range
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate random share prices between 100 and 500
    prices = np.random.uniform(100, 500, size=periods)
    
    # Create a DataFrame
    df = pd.DataFrame({'Date': dates, 'Price': prices})
    
    # Plot the share prices
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Price'], marker='o', linestyle='-')
    ax.set_title('Share Prices Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage
df, ax = task_func()
plt.show()