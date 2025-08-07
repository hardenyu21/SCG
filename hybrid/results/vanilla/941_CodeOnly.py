import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate a date range starting from the given date
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate random sales data
    # Here, we assume sales follow a normal distribution with a mean of 100 and a standard deviation of 20
    sales = np.random.normal(loc=100, scale=20, size=periods)
    
    # Create a DataFrame with the generated dates and sales
    forecast_df = pd.DataFrame({'Date': dates, 'Sales': sales})
    
    # Plot the sales forecast
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(forecast_df['Date'], forecast_df['Sales'], marker='o', linestyle='-')
    ax.set_title('Sales Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the DataFrame and the Axes object
    return forecast_df, ax

# Example usage:
# df, ax = task_func('2023-01-01', 12, 'M')
# plt.show()