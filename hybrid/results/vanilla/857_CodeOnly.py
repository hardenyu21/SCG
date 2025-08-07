import warnings
import os
import glob
import shutil

def task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS):
    transferred_files = []

    # Ensure the destination directory exists
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    # Iterate over each specified extension
    for ext in EXTENSIONS:
        # Create a pattern to match files with the current extension
        pattern = os.path.join(SOURCE_DIR, f'*.{ext}')
        
        # Find all files matching the pattern
        files = glob.glob(pattern)
        
        # Attempt to transfer each file
        for file in files:
            try:
                # Extract the file name
                file_name = os.path.basename(file)
                
                # Define the destination file path
                dest_file = os.path.join(DEST_DIR, file_name)
                
                # Copy the file to the destination directory
                shutil.copy2(file, dest_file)
                
                # Add the file name to the list of transferred files
                transferred_files.append(file_name)
            except Exception as e:
                # Issue a warning if the file could not be transferred
                warnings.warn(f"Could not transfer file {file}: {e}")

    return transferred_files