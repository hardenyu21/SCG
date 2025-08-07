import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(epoch_milliseconds, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Convert epoch milliseconds to a datetime object
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    
    # Get the current system time
    current_time = datetime.now()
    
    # Check if the start time is after the current system time
    if start_time > current_time:
        raise ValueError("The start time is after the current system time.")
    
    # Predefined lists for users and activities
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    activities = ['login', 'logout', 'browse', 'search', 'purchase']
    
    # Initialize a list to store log entries
    logs = []
    
    # Initialize the current time for logging
    current_log_time = start_time
    
    # Generate log entries until the current system time
    while current_log_time <= current_time:
        # Randomly choose a user and an activity
        user = random.choice(users)
        activity = random.choice(activities)
        
        # Append the log entry to the list
        logs.append({
            'User': user,
            'Activity': activity,
            'Time': current_log_time
        })
        
        # Increment the current log time by a random number of seconds (1 to 10)
        increment_seconds = random.randint(1, 10)
        current_log_time += timedelta(seconds=increment_seconds)
    
    # Create a DataFrame from the log entries
    df = pd.DataFrame(logs)
    
    return df