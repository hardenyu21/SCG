import subprocess
import os
import shutil
import sys

# Constants
DIRECTORY = 'c:\\Program Files\\VMware\\VMware Server'
BACKUP_DIRECTORY = 'c:\\Program Files\\VMware\\VMware Server\\Backup'

def task_func(filename):
    # Construct full file paths
    source_file = os.path.join(DIRECTORY, filename)
    backup_file = os.path.join(BACKUP_DIRECTORY, filename)

    # Ensure the backup directory exists
    if not os.path.exists(BACKUP_DIRECTORY):
        try:
            os.makedirs(BACKUP_DIRECTORY)
        except OSError as e:
            print(f"Failed to create backup directory: {e}", file=sys.stderr)
            return -1

    # Backup the file
    try:
        shutil.copy2(source_file, backup_file)
    except IOError as e:
        print(f"Failed to backup file: {e}", file=sys.stderr)
        return -1

    # Execute the file as a subprocess
    try:
        result = subprocess.run([source_file], check=False)
        return result.returncode
    except Exception as e:
        print(f"Failed to execute file: {e}", file=sys.stderr)
        return -1

# Example usage:
# exit_code = task_func('example.exe')
# print(f"Subprocess exit code: {exit_code}")