import pandas as pd
from datetime import datetime, timedelta
from random import randint, seed as random_seed

def task_func(start_date=datetime(2020, 1, 1), end_date=datetime(2020, 12, 31), seed=42):
    # Validate input types
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("Both 'start_date' and 'end_date' must be datetime.datetime instances.")
    
    # Validate date order
    if start_date > end_date:
        raise ValueError("'start_date' must be earlier than or equal to 'end_date'.")
    
    # Calculate the number of days in the range
    num_days = (end_date - start_date).days + 1
    
    # Set the random seed for reproducibility
    random_seed(seed)
    
    # Generate random dates within the range
    random_dates = [start_date + timedelta(days=randint(0, num_days - 1)) for _ in range(num_days)]
    
    # Create a pandas Series from the list of random dates
    date_series = pd.Series(random_dates)
    
    return date_series

# Example usage:
# series = task_func(datetime(2020, 1, 1), datetime(2020, 12, 31), seed=42)
# print(series)