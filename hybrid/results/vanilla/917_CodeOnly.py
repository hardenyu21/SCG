import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    # Ensure the DataFrame has a 'Date' column and a 'Close' column
    if 'Date' not in df.columns or 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Date' and 'Close' columns.")
    
    # Set the 'Date' column as the index
    df.set_index('Date', inplace=True)
    
    # Fit the ARIMA model
    model = ARIMA(df['Close'], order=(5, 1, 0))  # Example order, can be tuned
    model_fit = model.fit()
    
    # Forecast the next 7 days
    forecast = model_fit.forecast(steps=7)
    
    # Plot the forecast
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['Close'], label='Historical Prices')
    ax.plot(forecast.index, forecast, label='Forecasted Prices', color='red')
    ax.set_title('Share Closing Price Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    ax.legend()
    
    # Return the forecasted prices and the Axes object
    return forecast.tolist(), ax