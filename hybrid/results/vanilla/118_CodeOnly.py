import os
import shutil

def task_func(directory, backup_directory):
    # Ensure the backup directory exists
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    copied_files = []
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Construct full file paths
            source_file = os.path.join(directory, filename)
            backup_file = os.path.join(backup_directory, filename)
            
            # Copy the file to the backup directory
            shutil.copy2(source_file, backup_file)
            
            # Add the path of the copied file to the list
            copied_files.append(backup_file)
    
    return copied_files