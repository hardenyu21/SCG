import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Create a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate a synthetic sales time-series
    np.random.seed(0)  # For reproducibility
    trend = np.linspace(100, 500, periods)  # Linear trend
    seasonal = np.sin(np.linspace(0, 2 * np.pi, periods)) * 50  # Seasonal component
    noise = np.random.normal(0, 10, periods)  # Random noise
    
    if model == 'additive':
        sales = trend + seasonal + noise
    elif model == 'multiplicative':
        sales = trend * (1 + seasonal / 100) * (1 + noise / 100)
    else:
        raise ValueError("Model must be either 'additive' or 'multiplicative'")
    
    # Create a DataFrame
    sales_series = pd.Series(sales, index=date_range)
    
    # Decompose the time-series
    decomposition = seasonal_decompose(sales_series, model=model, period=12)
    
    # Extract components
    trend_component = decomposition.trend
    seasonal_component = decomposition.seasonal
    residual_component = decomposition.resid
    
    # Return the components as a dictionary
    return {
        'trend': trend_component,
        'seasonal': seasonal_component,
        'residual': residual_component
    }

# Example usage
result = task_func('2020-01-01', 24, 'M', 'multiplicative')
print(len(result['seasonal']))  # Should output 24