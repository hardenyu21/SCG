import os
import shutil

# Constants
BACKUP_DIR = '/tmp/backup'

def task_func(directory):
    # Check if the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        return f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'
    
    # Construct the backup file path
    backup_file = os.path.join(BACKUP_DIR, os.path.basename(directory) + '.tar.gz')
    
    # Check if the backup file exists
    if not os.path.exists(backup_file):
        return f'Backup file for {directory} does not exist in {BACKUP_DIR}. Cannot rollback update.'
    
    # Check if the target directory exists
    if os.path.exists(directory):
        # Remove the existing directory to prepare for restoration
        shutil.rmtree(directory)
    
    # Extract the backup to the original directory
    try:
        shutil.unpack_archive(backup_file, directory)
    except Exception as e:
        return f'Failed to restore directory {directory} from backup: {str(e)}'
    
    return directory