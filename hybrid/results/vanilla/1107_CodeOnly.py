from datetime import datetime
import pytz

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(unix_timestamp, target_timezone):
    # Convert the Unix timestamp to a datetime object in UTC
    utc_dt = datetime.utcfromtimestamp(unix_timestamp)
    
    # Localize the UTC datetime to UTC timezone
    utc_dt = pytz.utc.localize(utc_dt)
    
    # Convert the datetime to the target timezone
    target_tz = pytz.timezone(target_timezone)
    target_dt = utc_dt.astimezone(target_tz)
    
    # Format the datetime object to the specified string format
    formatted_date = target_dt.strftime(DATE_FORMAT)
    
    return formatted_date