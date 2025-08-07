import re
import os
import zipfile

def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    extracted_dirs = []
    
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        # Check if the filename matches the given pattern
        match = re.match(pattern, filename)
        if match:
            # Extract the prefix part of the filename
            prefix = match.group(1)
            # Create the full path for the extraction directory
            extract_dir = os.path.join(directory, prefix)
            
            # Ensure the extraction directory exists
            os.makedirs(extract_dir, exist_ok=True)
            
            # Construct the full path to the zip file
            zip_path = os.path.join(directory, filename)
            
            # Extract the contents of the zip file into the extraction directory
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
            
            # Add the extraction directory to the list
            extracted_dirs.append(extract_dir)
    
    return extracted_dirs