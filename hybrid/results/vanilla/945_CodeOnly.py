import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', sales_data=None):
    # Generate a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # If sales_data is not provided, generate some random sales data
    if sales_data is None:
        sales_data = np.random.randint(100, 1000, size=periods)
    
    # Create a DataFrame with the date range and sales data
    df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    
    # Prepare the data for linear regression
    df['Time'] = np.arange(len(df))
    X = df[['Time']]
    y = df['Sales']
    
    # Fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Forecast future sales for the same number of periods
    future_time = np.arange(len(df), len(df) + periods).reshape(-1, 1)
    forecasted_sales = model.predict(future_time)
    
    return forecasted_sales

# Example usage:
# forecasted_sales = task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI')
# print(forecasted_sales)