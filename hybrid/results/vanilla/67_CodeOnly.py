import pandas as pd
import re
import os

def task_func(dir_path: str, pattern: str = '^EMP'):
    # Compile the regex pattern for matching file names
    regex = re.compile(pattern)
    
    # List to store file names and their sizes
    file_data = []
    
    # Iterate over all files in the directory
    for file_name in os.listdir(dir_path):
        # Check if the file name matches the pattern
        if regex.match(file_name):
            # Get the full path of the file
            file_path = os.path.join(dir_path, file_name)
            # Check if it's a file and not a directory
            if os.path.isfile(file_path):
                # Get the size of the file
                file_size = os.path.getsize(file_path)
                # Append the file name and size to the list
                file_data.append({'File': file_name, 'Size': file_size})
    
    # Sort the file data by file name
    file_data.sort(key=lambda x: x['File'])
    
    # Create a pandas DataFrame from the file data
    df = pd.DataFrame(file_data)
    
    return df