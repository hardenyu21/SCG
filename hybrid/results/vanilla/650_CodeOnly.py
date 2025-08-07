from datetime import datetime, timedelta
import pytz
from dateutil.parser import parse

def task_func(date_str, tz_str):
    # Parse the input date string into a datetime object
    date = parse(date_str)
    
    # Localize the datetime object to the specified timezone
    timezone = pytz.timezone(tz_str)
    localized_date = timezone.localize(date)
    
    # Calculate the next New Year's Day in the same timezone
    next_new_year = datetime(localized_date.year + 1, 1, 1, tzinfo=timezone)
    
    # Calculate the difference in seconds until the next New Year
    time_until_next_new_year = (next_new_year - localized_date).total_seconds()
    
    return int(time_until_next_new_year)

# Example usage:
# print(task_func("2023-12-31T23:00:00", "America/New_York"))