import os
import glob
import shutil
import time

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:
    # Calculate the cutoff time in seconds since the epoch
    cutoff_time = time.time() - (days_old * 24 * 60 * 60)
    
    # Create the archive directory if it doesn't exist
    archive_dir = os.path.join(my_path, 'archive')
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Iterate over each file extension
    for ext in FILE_EXTENSIONS:
        # Find all files with the current extension in the directory
        search_pattern = os.path.join(my_path, f'*{ext}')
        for file_path in glob.glob(search_pattern):
            # Check if the file was last modified before the cutoff time
            if os.path.getmtime(file_path) < cutoff_time:
                # Move the file to the archive directory
                shutil.move(file_path, archive_dir)
    
    # Return the path of the archive directory
    return archive_dir