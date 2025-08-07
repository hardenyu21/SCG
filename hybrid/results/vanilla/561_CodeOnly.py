import pytz
from dateutil import parser

def task_func(date_str, from_tz, to_tz):
    # Parse the input date string into a datetime object
    naive_datetime = parser.parse(date_str)
    
    # Localize the naive datetime to the source timezone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Convert the localized datetime to the target timezone
    to_timezone = pytz.timezone(to_tz)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    
    # Format the converted datetime as a string in "yyyy-mm-dd hh:mm:ss" format
    formatted_datetime = converted_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_datetime