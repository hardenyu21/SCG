import os
import pandas as pd
import re

def task_func(file_path: str) -> pd.DataFrame:
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified log file does not exist: {file_path}")
    
    # Define the regular expression pattern for log entries
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}) - (\w+) - (.*)')
    
    # Initialize lists to store extracted data
    timestamps = []
    levels = []
    messages = []
    
    # Open and read the log file line by line
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                timestamp, level, message = match.groups()
                timestamps.append(timestamp)
                levels.append(level)
                messages.append(message)
    
    # Create a DataFrame from the extracted data
    log_df = pd.DataFrame({
        'Timestamp': timestamps,
        'Level': levels,
        'Message': messages
    })
    
    return log_df