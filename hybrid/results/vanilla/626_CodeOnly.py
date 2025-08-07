from random import choice
import pytz
from dateutil.parser import parse

# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']

def task_func(date_str, from_tz):
    # Parse the input date string into a datetime object
    naive_datetime = parse(date_str)
    
    # Localize the naive datetime to the source timezone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Choose a random timezone from the list
    to_tz = choice(TIMEZONES)
    
    # Convert the localized datetime to the randomly chosen timezone
    to_timezone = pytz.timezone(to_tz)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    
    # Format the converted datetime as a string
    converted_datetime_str = converted_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    return (converted_datetime_str, to_tz)

# Example usage:
# result = task_func('2023-10-01 12:00:00', 'UTC')
# print(result)