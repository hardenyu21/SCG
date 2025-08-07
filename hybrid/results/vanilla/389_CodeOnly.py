import re
import os
import shutil

def task_func(directory):
    # Define the pattern to search for filenames containing "like" or "what"
    pattern = re.compile(r'like|what', re.IGNORECASE)
    
    # Create the "Interesting Files" subdirectory if it doesn't exist
    interesting_files_dir = os.path.join(directory, "Interesting Files")
    if not os.path.exists(interesting_files_dir):
        os.makedirs(interesting_files_dir)
    
    # List to store the names of files moved
    moved_files = []
    
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        # Check if the filename contains "like" or "what"
        if pattern.search(filename):
            # Construct full file paths
            src_file = os.path.join(directory, filename)
            dst_file = os.path.join(interesting_files_dir, filename)
            
            # Move the file to the "Interesting Files" subdirectory
            shutil.move(src_file, dst_file)
            
            # Add the filename to the list of moved files
            moved_files.append(filename)
    
    # Output the list of files moved
    return moved_files