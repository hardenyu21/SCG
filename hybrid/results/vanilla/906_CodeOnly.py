import zipfile
import os
import re
import shutil

def task_func(source_dir: str, target_dir: str, archive_name: str = 'archive.zip') -> str:
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Define the path for the archive
    archive_path = os.path.join(target_dir, archive_name)

    # Create a new zip file
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        # Iterate over all files in the source directory
        for root, _, files in os.walk(source_dir):
            for file in files:
                # Check if the file is processed by looking for '_processed' suffix
                if re.search(r'_processed$', file):
                    # Construct the full file path
                    file_path = os.path.join(root, file)
                    # Add the file to the archive
                    archive.write(file_path, os.path.relpath(file_path, source_dir))

    return archive_path