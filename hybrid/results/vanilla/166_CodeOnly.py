import pandas as pd
from datetime import datetime, timedelta
import holidays

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    # Validate input dates
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime object.")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime object.")
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date.")
    if end_date < start_date:
        raise ValueError("end_date must not be before start_date.")
    
    # Create a range of dates from start_date to end_date
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Get public holidays for the specified country
    try:
        country_holidays = holidays.CountryHoliday(country, years=[start_date.year, end_date.year])
    except KeyError:
        raise ValueError(f"Invalid country code: {country}")
    
    # Filter out weekends and public holidays
    business_days = [
        date for date in date_range
        if date.weekday() < 5 and date not in country_holidays
    ]
    
    return business_days

# Example usage:
# business_days = task_func(datetime(2023, 1, 1), datetime(2023, 12, 31), 'US')
# print(business_days)