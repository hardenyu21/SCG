from datetime import datetime
import pytz
import numpy as np

def task_func(time_strings, timezone):
    # Convert the timezone string to a timezone object
    tz = pytz.timezone(timezone)
    
    # Convert each timestamp string to a datetime object in the specified timezone
    try:
        timestamps = [datetime.fromisoformat(ts).astimezone(tz) for ts in time_strings]
    except ValueError:
        # If there's an error in parsing the timestamps, return 0.0
        return 0.0
    
    # If there are less than two timestamps, return 0.0
    if len(timestamps) < 2:
        return 0.0
    
    # Calculate the absolute time difference in seconds between each consecutive pair
    time_differences = []
    for i in range(1, len(timestamps)):
        diff = abs((timestamps[i] - timestamps[i - 1]).total_seconds())
        time_differences.append(diff)
    
    # If there are no time differences, return 0.0
    if not time_differences:
        return 0.0
    
    # Calculate the mean of the time differences
    mean_time_difference = np.mean(time_differences)
    
    return mean_time_difference