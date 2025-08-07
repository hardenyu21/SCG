import subprocess
import shlex
from datetime import datetime

def task_func(script_path: str) -> dict:
    # Record the start time
    start_time = datetime.now()
    
    # Prepare the command to run the R script
    command = f"Rscript {shlex.quote(script_path)}"
    
    # Run the command using subprocess
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Capture the stdout and stderr
    stdout, stderr = process.communicate()
    
    # Record the end time
    end_time = datetime.now()
    
    # Prepare the result dictionary
    result = {
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "stdout": stdout,
        "stderr": stderr
    }
    
    return result