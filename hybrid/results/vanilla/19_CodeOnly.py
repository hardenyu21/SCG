import os
import glob
import zipfile

def task_func(directory):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The specified directory '{directory}' does not exist.")
    
    # Find all files in the directory (not including subdirectories)
    files = glob.glob(os.path.join(directory, '*'))
    files = [f for f in files if os.path.isfile(f)]
    
    # If there are no files, return None
    if not files:
        return None
    
    # Define the path for the zip file
    zip_path = os.path.join(directory, 'files.zip')
    
    # Create a zip file and add all files to it
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    
    # Return the path to the created zip file
    return zip_path