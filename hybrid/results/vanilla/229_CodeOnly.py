import json
import random
from datetime import datetime, timedelta

# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
ACTIONS = ['login', 'logout', 'view', 'edit', 'delete']

def task_func(file_path, num_entries, seed=None):
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Generate the list of log entries
    log_entries = []
    start_time = datetime.now() - timedelta(days=30)  # Start 30 days ago
    
    for _ in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(ACTIONS)
        timestamp = start_time + timedelta(seconds=random.randint(0, 30 * 24 * 3600))
        log_entries.append({
            'user': user,
            'action': action,
            'timestamp': timestamp.isoformat()
        })
    
    # Write the log entries to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(log_entries, json_file, indent=4)
    
    # Return the file path
    return file_path