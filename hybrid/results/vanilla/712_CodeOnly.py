import os
import shutil
import glob

def task_func(source_dir, dest_dir, extension):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Construct the search pattern for files with the given extension
    search_pattern = os.path.join(source_dir, f'*.{extension}')
    
    # Find all files matching the pattern
    files_to_move = glob.glob(search_pattern)
    
    # Initialize a counter for the number of files moved
    result = 0
    
    # Move each file to the destination directory
    for file_path in files_to_move:
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        
        # Construct the destination file path
        dest_file_path = os.path.join(dest_dir, file_name)
        
        # Move the file
        shutil.move(file_path, dest_file_path)
        
        # Increment the counter
        result += 1
    
    # Return the count of files moved
    return result