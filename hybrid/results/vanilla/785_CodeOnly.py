import subprocess
import os
import glob
import shutil
import zipfile

# Constants
ARCHIVE_DIR = '/tmp/archive'

def task_func(pattern):
    # Ensure the archive directory exists
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    # Find all files matching the pattern
    files_to_archive = glob.glob(pattern)
    
    if not files_to_archive:
        raise FileNotFoundError(f"No files found matching the pattern: {pattern}")

    # Create a unique archive file name
    archive_name = os.path.basename(pattern).replace('*', '_') + '.zip'
    archive_file = os.path.join(ARCHIVE_DIR, archive_name)

    # Create a zip archive of the files
    with zipfile.ZipFile(archive_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_archive:
            zipf.write(file, os.path.basename(file))
            os.remove(file)  # Delete the original file after adding to the archive

    return archive_file