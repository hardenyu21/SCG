import os
import shutil
import tempfile

# Constants
BACKUP_DIR = '/tmp/backup'

def get_unique_backup_dir():
    # Create a unique backup directory path
    return tempfile.mkdtemp(dir=BACKUP_DIR)

def task_func(directory):
    errors = []
    backup_dir = None

    try:
        # Ensure the backup directory exists
        os.makedirs(BACKUP_DIR, exist_ok=True)

        # Get a unique backup directory path
        backup_dir = get_unique_backup_dir()

        # Copy the directory to the backup location
        shutil.copytree(directory, backup_dir)

        # Clean the original directory
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(directory)

    except Exception as e:
        errors.append(str(e))

    return backup_dir, errors

# Example usage:
# backup_path, errors = task_func('/path/to/directory')
# print(f"Backup Path: {backup_path}")
# print(f"Errors: {errors}")