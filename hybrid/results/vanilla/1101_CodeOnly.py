import subprocess
import os
import glob
import time

def task_func(test_dir):
    execution_times = {}
    
    # Ensure the directory exists
    if not os.path.isdir(test_dir):
        raise ValueError(f"The directory {test_dir} does not exist.")
    
    # Find all Python files in the directory
    python_files = glob.glob(os.path.join(test_dir, '*.py'))
    
    for file_path in python_files:
        file_name = os.path.basename(file_path)
        
        # Record the start time
        start_time = time.time()
        
        try:
            # Run the Python script
            subprocess.run(['python', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {file_name}: {e}")
        
        # Record the end time
        end_time = time.time()
        
        # Calculate the execution time
        execution_time = end_time - start_time
        
        # Store the execution time in the dictionary
        execution_times[file_name] = execution_time
    
    return execution_times