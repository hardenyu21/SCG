import os
import logging

def task_func(directory):
    # Set up logging
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO, 
                        format='%(asctime)s - %(message)s')
    
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The specified directory '{directory}' does not exist.")
    
    # Initialize counters and list for removed files
    files_removed = 0
    removed_files_list = []
    
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JavaScript file containing 'jquery' in its name
        if filename.lower().endswith('.js') and 'jquery' in filename.lower():
            file_path = os.path.join(directory, filename)
            try:
                # Remove the file
                os.remove(file_path)
                # Log the removal
                logging.info(f"Removed file: {file_path}")
                # Update counters and list
                files_removed += 1
                removed_files_list.append(filename)
            except Exception as e:
                # Log any errors that occur during file removal
                logging.error(f"Error removing file {file_path}: {e}")
    
    # Return the result as a tuple
    return files_removed, removed_files_list