import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    # Ensure the destination directory exists
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # Define the patterns to match
    patterns = ['*.txt', '*.docx']
    
    # Iterate over all files in the source directory
    for root, dirs, files in os.walk(src_dir):
        for pattern in patterns:
            for filename in fnmatch.filter(files, pattern):
                # Construct full file paths
                src_file = os.path.join(root, filename)
                dst_file = os.path.join(dst_dir, filename)
                
                # Copy the file to the destination directory
                shutil.copy2(src_file, dst_file)
    
    # Return the destination directory
    return dst_dir