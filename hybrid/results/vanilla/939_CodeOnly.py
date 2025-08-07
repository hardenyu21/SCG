import re
import os
import glob

def task_func(dir_path: str) -> list:
    # Compile a regular expression pattern to match all non-alphanumeric characters
    pattern = re.compile(r'[^a-zA-Z0-9]')
    
    # List to store the new file names
    new_file_names = []
    
    # Get all files in the specified directory
    for file_path in glob.glob(os.path.join(dir_path, '*')):
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        
        # Remove all non-alphanumeric characters from the file name
        new_file_name = pattern.sub('', file_name)
        
        # Construct the new file path
        new_file_path = os.path.join(dir_path, new_file_name)
        
        # Rename the file if the new file name is different from the old one
        if new_file_name != file_name:
            os.rename(file_path, new_file_path)
        
        # Add the new file name to the list
        new_file_names.append(new_file_name)
    
    return new_file_names