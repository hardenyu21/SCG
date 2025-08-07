import pytz
from dateutil.parser import parse

def task_func(date_str, from_tz, to_tz):
    # Parse the date string into a datetime object
    naive_datetime = parse(date_str)
    
    # Localize the naive datetime to the source time zone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Convert the localized datetime to the destination time zone
    to_timezone = pytz.timezone(to_tz)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    
    # Get the current time in the destination time zone
    current_time = to_timezone.localize(parse('now'))
    
    # Calculate the time difference in seconds
    time_difference = (current_time - converted_datetime).total_seconds()
    
    return int(time_difference)