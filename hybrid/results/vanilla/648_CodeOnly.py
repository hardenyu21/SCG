from dateutil.parser import parse
from datetime import timedelta

def task_func(date_str):
    # Parse the input date string into a datetime object
    date = parse(date_str)
    
    # Initialize a variable to hold the next business day
    next_business_day = date
    
    # Loop until we find the next business day (Monday to Friday)
    while True:
        # Move to the next day
        next_business_day += timedelta(days=1)
        
        # Check if the next day is a weekday (Monday=0, Sunday=6)
        if next_business_day.weekday() < 5:
            break
    
    return next_business_day