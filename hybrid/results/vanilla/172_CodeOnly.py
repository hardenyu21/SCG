import json
from datetime import datetime

def task_func(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    
    # Extract the 'utc_datetime' value
    utc_datetime_str = data.get('utc_datetime')
    
    # Convert the string to a datetime object
    utc_datetime = datetime.fromisoformat(utc_datetime_str)
    
    # Determine if the date is a weekend (Saturday or Sunday)
    # weekday() returns 5 for Saturday and 6 for Sunday
    is_weekend = utc_datetime.weekday() in (5, 6)
    
    return is_weekend