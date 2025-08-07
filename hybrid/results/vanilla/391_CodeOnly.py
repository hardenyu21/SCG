import os
import glob
import shutil

def task_func(directory, archive_dir='archive'):
    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Find all JSON files in the given directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    
    # Initialize a list to store error messages
    error_messages = []

    # Iterate over each JSON file
    for file_path in json_files:
        try:
            # Construct the destination path
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(archive_dir, file_name)
            
            # Move the file to the archive directory
            shutil.move(file_path, destination_path)
        except Exception as e:
            # If an error occurs, add a message to the error list
            error_messages.append(f"Failed to move {file_path}: {str(e)}")

    # Determine if all files were successfully moved
    all_files_moved = len(error_messages) == 0

    # Return the result as a tuple
    return (all_files_moved, error_messages)