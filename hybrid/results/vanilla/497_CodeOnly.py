from datetime import datetime, timedelta
import pytz
import calendar

def task_func(days_in_past=7):
    if days_in_past < 0:
        raise ValueError("days_in_past must be a non-negative integer.")
    
    # Get the current date in UTC
    utc_now = datetime.now(pytz.utc)
    
    # Calculate the date 'days_in_past' days ago
    target_date = utc_now - timedelta(days=days_in_past)
    
    # Get the weekday as an integer (0=Monday, 6=Sunday)
    weekday_index = target_date.weekday()
    
    # Get the weekday name
    weekday_name = calendar.day_name[weekday_index]
    
    return weekday_name