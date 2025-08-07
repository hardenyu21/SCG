import re
from datetime import datetime, time

def task_func(logs: list):
    error_times = []
    
    # Regular expression to find error logs and extract time
    error_pattern = re.compile(r'ERROR.*?(\d{2}:\d{2}:\d{2})')
    
    for log in logs:
        match = error_pattern.search(log)
        if match:
            # Extract the time string and convert it to a datetime.time object
            time_str = match.group(1)
            error_time = datetime.strptime(time_str, '%H:%M:%S').time()
            error_times.append(error_time)
    
    # Calculate the average time of occurrence of errors
    if error_times:
        total_seconds = sum((dt.hour * 3600 + dt.minute * 60 + dt.second) for dt in error_times)
        average_seconds = total_seconds // len(error_times)
        average_time = time(hour=average_seconds // 3600, minute=(average_seconds % 3600) // 60, second=average_seconds % 60)
    else:
        average_time = None
    
    return error_times, average_time

# Example usage:
logs = [
    "2023-10-01 12:34:56 INFO: System started",
    "2023-10-01 12:35:01 ERROR: Failed to load module",
    "2023-10-01 12:36:00 INFO: Processing data",
    "2023-10-01 12:37:00 ERROR: Connection timeout",
    "2023-10-01 12:38:00 INFO: Data processed"
]

error_times, average_time = task_func(logs)
print("Error Times:", error_times)
print("Average Time of Errors:", average_time)