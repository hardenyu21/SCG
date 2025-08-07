import os
import re

def task_func(pattern, log_dir='/var/log/'):
    # Compile the regex pattern for matching
    regex = re.compile(pattern)
    
    # Initialize variables to track the most recent file and its modification time
    most_recent_file = None
    most_recent_mtime = -1
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(log_dir):
        # Construct the full path to the file
        file_path = os.path.join(log_dir, filename)
        
        # Check if the file matches the regex pattern
        if regex.match(filename):
            # Get the modification time of the file
            mtime = os.path.getmtime(file_path)
            
            # Update the most recent file if this one is more recent
            if mtime > most_recent_mtime:
                most_recent_file = file_path
                most_recent_mtime = mtime
    
    # Return the path to the most recent file, or None if no matching files were found
    return most_recent_file