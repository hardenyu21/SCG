import re
import os
import shutil

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Compile the regex pattern for matching file names
    pattern = re.compile(file_pattern)
    
    # Initialize a counter for the number of moved files
    moved_files_count = 0
    
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        # Construct the full file path
        source_file_path = os.path.join(source_dir, filename)
        
        # Check if it's a file and if its name matches the pattern
        if os.path.isfile(source_file_path) and pattern.match(filename):
            # Construct the target file path
            target_file_path = os.path.join(target_dir, filename)
            
            # Move the file to the target directory
            shutil.move(source_file_path, target_file_path)
            
            # Increment the counter
            moved_files_count += 1
    
    # Return the count of moved files
    return moved_files_count