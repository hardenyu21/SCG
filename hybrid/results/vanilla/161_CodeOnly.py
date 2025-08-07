import re
import pandas as pd
from datetime import datetime

def task_func(log_file):
    # Define the regex pattern for log entries
    log_pattern = re.compile(r'^(?P<type>\w+): \[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] - (?P<message>.*)$')
    
    # Initialize a list to store valid log entries
    valid_logs = []
    
    # Read the log file line by line
    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.match(line.strip())
            if match:
                log_entry = match.groupdict()
                try:
                    # Validate the timestamp
                    datetime.strptime(log_entry['timestamp'], '%Y-%m-%d %H:%M:%S')
                    valid_logs.append(log_entry)
                except ValueError:
                    # Raise an exception if the timestamp is invalid
                    raise ValueError(f"Invalid timestamp in log entry: {line.strip()}")
    
    # Check if any valid log entries were found
    if not valid_logs:
        raise ValueError("No valid log entries found in the log file.")
    
    # Create a DataFrame from the valid log entries
    df = pd.DataFrame(valid_logs)
    
    # Define the output CSV file path
    csv_file = 'structured_logs.csv'
    
    # Write the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    
    # Return the file path to the newly created CSV file
    return csv_file