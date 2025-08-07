import numpy as np
import random
from datetime import datetime, timedelta

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Calculate the total number of days between start_date and end_date
    delta = end_date - start_date
    total_days = delta.days + 1
    
    # Ensure the number of unique dates required does not exceed the available days
    if rows * columns > total_days:
        raise ValueError("The number of unique dates requested exceeds the available days between start_date and end_date.")
    
    # Generate a list of unique dates
    unique_dates = [start_date + timedelta(days=i) for i in range(total_days)]
    random.shuffle(unique_dates)
    
    # Select the required number of unique dates
    selected_dates = unique_dates[:rows * columns]
    
    # Reshape the list of dates into a numpy ndarray
    date_matrix = np.array(selected_dates).reshape(rows, columns)
    
    return date_matrix

# Example usage:
# date_matrix = task_func(3, 2, datetime(2021, 1, 1), datetime(2021, 12, 31), seed=0)
# print(date_matrix)