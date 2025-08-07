import pytz
from dateutil.parser import parse

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_string, from_tz, to_tz):
    # Parse the input time string into a datetime object
    naive_datetime = parse(time_string)
    
    # Localize the naive datetime to the source timezone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Convert the localized datetime to the target timezone
    to_timezone = pytz.timezone(to_tz)
    converted_datetime = localized_datetime.astimezone(to_timezone)
    
    # Format the converted datetime to the desired string format
    converted_time_string = converted_datetime.strftime(TIME_FORMAT)
    
    return converted_time_string

# Example usage:
# print(task_func("01/01/22 12:00:00.000", "America/New_York", "Europe/London"))