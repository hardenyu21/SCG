import pytz
import numpy as np
from dateutil.parser import parse
import math

MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    # Parse the date string and convert it to the target timezone
    date = parse(date_str)
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    date = from_timezone.localize(date).astimezone(to_timezone)
    
    # Calculate the number of days since the first reference year
    reference_year = MOON_PHASES_YEARS[0]
    days_since_reference = (date - datetime.datetime(reference_year, 1, 1, tzinfo=to_timezone)).days
    
    # Calculate the moon phase
    # The moon phase cycle is approximately 29.53 days
    lunar_cycle_days = 29.53
    moon_phase = (days_since_reference % lunar_cycle_days) / lunar_cycle_days
    
    return moon_phase

# Example usage:
# print(task_func("2023-10-01T12:00:00", "UTC", "America/New_York"))