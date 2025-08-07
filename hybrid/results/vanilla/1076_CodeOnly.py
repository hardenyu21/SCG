from datetime import datetime
import pandas as pd

# For Python versions lower than 3.9, use 'pytz' instead of 'zoneinfo'
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo

TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_strings, target_tz):
    # Initialize lists to store original and converted times
    original_times = []
    converted_times = []
    
    # Iterate over each time string in the input list
    for time_str in time_strings:
        # Parse the UTC time string into a datetime object
        utc_time = datetime.strptime(time_str, TIME_FORMAT)
        
        # Convert the UTC time to the specified timezone
        target_timezone = ZoneInfo(target_tz)
        converted_time = utc_time.astimezone(target_timezone)
        
        # Append the original and converted times to their respective lists
        original_times.append(utc_time)
        converted_times.append(converted_time)
    
    # Create a DataFrame with the original and converted times
    df = pd.DataFrame({
        'Original Time': original_times,
        'Converted Time': converted_times
    })
    
    return df

# Example usage:
# time_strings = ["01/01/22 12:00:00.000000", "02/01/22 13:30:00.000000"]
# target_tz = "America/New_York"
# df = task_func(time_strings, target_tz)
# print(df)