import os
import errno
import shutil

def task_func(filename, dest_dir):
    try:
        # Ensure the destination directory exists
        os.makedirs(dest_dir, exist_ok=True)
        
        # Construct the full path for the destination file
        dest_file_path = os.path.join(dest_dir, os.path.basename(filename))
        
        # Copy the file to the destination directory
        shutil.copy2(filename, dest_file_path)
        
        # Open the original file in write mode to clear its contents
        with open(filename, 'w') as file:
            file.truncate(0)
        
        # Return the absolute path to the copied file
        return os.path.abspath(dest_file_path)
    
    except OSError as e:
        # Raise an OSError if any of the file operations fail
        raise OSError(f"An error occurred: {e.strerror}") from e