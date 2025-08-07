import os
from datetime import datetime

# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):
    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except OSError as e:
            print(f"Error creating directory {log_dir}: {e}")
            return False

    # Construct the full file path
    file_path = os.path.join(log_dir, filename)

    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Prepare the log entry
    log_entry = f"{timestamp} - Metrics: {metrics}\n"

    try:
        # Open the file in append mode and write the log entry
        with open(file_path, 'a') as file:
            file.write(log_entry)
        return True
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")
        return False

# Example usage
metrics = {'precision': 0.75, 'recall': 0.80}
success = task_func(metrics, 'evaluation.log')
print(success)