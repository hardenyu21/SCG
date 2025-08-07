import pytz
import numpy as np
from dateutil.parser import parse
import math

SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    # Parse the date string and convert it to the specified timezone
    date = parse(date_str)
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    date = from_timezone.localize(date).astimezone(to_timezone)
    
    # Extract the year from the date
    year = date.year
    
    # Find the closest solar cycle year
    closest_cycle_year = SOLAR_CYCLE_YEARS[np.argmin(np.abs(SOLAR_CYCLE_YEARS - year))]
    
    # Calculate the number of years since the closest solar cycle year
    years_since_cycle = year - closest_cycle_year
    
    # Calculate solar activity using a cosine function
    # The cosine function will oscillate between -1 and 1, so we scale it to 0-1
    solar_activity = 0.5 * (1 + math.cos(2 * math.pi * years_since_cycle / 11))
    
    return solar_activity

# Example usage:
# print(task_func("2023-10-01T12:00:00", "UTC", "America/New_York"))