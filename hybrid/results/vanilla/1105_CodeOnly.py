import subprocess
import os
import time
import glob

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    # Start the timer
    start_time = time.time()
    
    # Execute the R script
    try:
        subprocess.run(['Rscript', r_script_path], check=True)
    except subprocess.CalledProcessError as e:
        return (False, f"Error executing R script: {e}")
    
    # Check if the output file is generated within the specified duration
    while time.time() - start_time < duration:
        # Check if the output file exists
        if os.path.exists(output_path):
            return (True, 'File generated successfully within the specified duration.')
        # Wait for a short period before checking again
        time.sleep(1)
    
    # If the loop completes, the file was not generated in time
    return (False, 'File not generated within the specified duration.')