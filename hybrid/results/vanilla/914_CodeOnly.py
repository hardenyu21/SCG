import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Ensure the DataFrame has a 'Date' column and a 'Close' column
    if 'Date' not in df.columns or 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Date' and 'Close' columns.")
    
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort the DataFrame by date
    df = df.sort_values('Date')
    
    # Extract the closing prices
    prices = df['Close'].values
    
    # Create a time index in seconds
    time_index = (df['Date'] - df['Date'].min()).dt.total_seconds().values.reshape(-1, 1)
    
    # Fit a linear regression model
    model = LinearRegression()
    model.fit(time_index, prices)
    
    # Predict the next 7 days
    future_days = 7
    last_timestamp = time_index[-1][0]
    future_timestamps = np.array([last_timestamp + 24 * 60 * 60 * i for i in range(1, future_days + 1)]).reshape(-1, 1)
    predicted_prices = model.predict(future_timestamps)
    
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['Date'], prices, label='Historical Prices', marker='o')
    ax.plot(pd.to_datetime(future_timestamps, unit='s') + df['Date'].min(), predicted_prices, label='Predicted Prices', marker='x')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    ax.set_title('Stock Closing Prices Prediction')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return predicted_prices.tolist(), ax

# Example usage:
# df = pd.DataFrame({
#     'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
#     'Close': np.random.rand(10) * 100
# })
# predicted_prices, ax = task_func(df)
# plt.show()