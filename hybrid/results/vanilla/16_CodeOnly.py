import os
import glob
import tarfile

def task_func(directory, backup_dir='/path/to/backup'):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The specified directory '{directory}' does not exist.")
    
    # Find all .log files in the specified directory
    log_files = glob.glob(os.path.join(directory, '*.log'))
    
    # If no log files are found, return the message
    if not log_files:
        return 'No logs found to backup'
    
    # Ensure the backup directory exists
    os.makedirs(backup_dir, exist_ok=True)
    
    # Define the path for the backup file
    backup_file_path = os.path.join(backup_dir, 'logs_backup.tar.gz')
    
    # Create a tar.gz file and add all log files to it
    with tarfile.open(backup_file_path, 'w:gz') as tar:
        for log_file in log_files:
            tar.add(log_file, arcname=os.path.basename(log_file))
    
    # Delete the original log files after backup
    for log_file in log_files:
        os.remove(log_file)
    
    # Return the path to the backup file
    return backup_file_path