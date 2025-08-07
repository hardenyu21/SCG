import subprocess
import os
import time
from datetime import datetime

def task_func(script_dir, scripts, delay):
    if delay < 0:
        raise ValueError("Delay must be non-negative.")
    if not scripts:
        raise ValueError("No scripts provided.")
    
    timestamps = []
    
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        if not os.path.isfile(script_path):
            print(f"Warning: Script {script} not found. Skipping.")
            continue
        
        # Record the start time
        start_time = datetime.now()
        timestamps.append(start_time)
        
        # Execute the script
        try:
            subprocess.run(['bash', script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing script {script}: {e}")
        
        # Wait for the specified delay
        time.sleep(delay)
    
    return timestamps