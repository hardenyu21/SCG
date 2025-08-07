from datetime import datetime
import pytz
import re
from faker import Faker

def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    # Initialize Faker with a seed for reproducibility
    fake = Faker()
    Faker.seed(seed)
    
    # Convert epoch milliseconds to datetime object in the current system timezone
    current_timezone = datetime.now().astimezone().tzinfo
    event_datetime = datetime.fromtimestamp(epoch_milliseconds / 1000, current_timezone)
    
    # Generate a fake event name
    event_name = fake.catch_phrase()
    
    # Validate and filter timezones
    valid_timezones = []
    for tz in timezones:
        if tz in pytz.all_timezones:
            valid_timezones.append(tz)
        elif re.match(r'^UTC[+-]\d{2}:\d{2}$', tz):
            valid_timezones.append(tz)
    
    # If no valid timezones are provided, use UTC
    if not valid_timezones:
        valid_timezones = ["UTC"]
    
    # Randomly select a valid timezone
    selected_timezone = fake.random_element(valid_timezones)
    
    # Create the event schedule
    event_schedule = {
        'date': event_datetime.strftime('%Y-%m-%d'),
        'time': event_datetime.strftime('%H:%M:%S'),
        'timezone': selected_timezone
    }
    
    # Return the dictionary with the fake event name and schedule
    return {event_name: [event_schedule]}

# Example usage:
# epoch_milliseconds = 1633072800000  # Example epoch time in milliseconds
# print(task_func(epoch_milliseconds))