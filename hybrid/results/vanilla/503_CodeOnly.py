import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def task_func(
    days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0
):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate a list of dates for the specified number of days in the past
    end_date = datetime.now()
    date_range = [end_date - timedelta(days=x) for x in range(days_in_past)]
    
    # Generate random stock prices for each stock and each day
    data = {
        "Date": date_range * len(stock_names),
        "Stock": np.repeat(stock_names, days_in_past),
        "Price": np.random.rand(days_in_past * len(stock_names))
    }
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame(data)
    
    # Set the 'Date' column as the index
    df.set_index("Date", inplace=True)
    
    return df

# Example usage
df = task_func(days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0)
print(df)