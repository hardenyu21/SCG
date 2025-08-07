import subprocess
import os
import json
from datetime import datetime

def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    # Check if the script file exists
    if not os.path.isfile(script_name):
        raise FileNotFoundError(f"The script file '{script_name}' does not exist.")
    
    # Record the start time
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        # Execute the script
        result = subprocess.run(['bash', script_name], check=True, capture_output=True, text=True)
        exit_status = result.returncode
    except subprocess.CalledProcessError as e:
        exit_status = e.returncode
        raise RuntimeError(f"An error occurred while executing the script: {e.stderr}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
    
    # Record the end time
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Prepare the log entry
    log_entry = {
        'start_time': start_time,
        'end_time': end_time,
        'exit_status': exit_status
    }
    
    # Write the log entry to the specified JSON log file
    try:
        with open(log_file, 'a') as f:
            json.dump(log_entry, f)
            f.write('\n')  # Ensure each log entry is on a new line
    except IOError as e:
        raise RuntimeError(f"An error occurred while writing to the log file: {e}")
    
    return log_entry