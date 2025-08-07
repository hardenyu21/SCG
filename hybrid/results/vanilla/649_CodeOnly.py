import numpy as np
import pandas as pd
from dateutil.parser import parse

def task_func(dates_str_list):
    # Define the weekday names in order
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Initialize a list to store the weekday names
    weekday_counts = [0] * 7
    
    # Iterate over each date string in the list
    for date_str in dates_str_list:
        # Parse the date string to a datetime object
        date = parse(date_str)
        # Get the weekday as an integer (0=Monday, 6=Sunday)
        weekday_index = date.weekday()
        # Increment the count for the corresponding weekday
        weekday_counts[weekday_index] += 1
    
    # Create a pandas Series with the weekday distribution
    weekday_series = pd.Series(weekday_counts, index=weekdays)
    
    return weekday_series

# Example usage:
# dates = ["2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06", "2023-10-07", "2023-10-08"]
# print(task_func(dates))