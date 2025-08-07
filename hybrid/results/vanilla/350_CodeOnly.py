import subprocess
import os
import shutil
from glob import glob

def task_func(src_folder, dst_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # Get all files in the source folder
    files = glob(os.path.join(src_folder, '*'))
    failed_files = []

    for file_path in files:
        if os.path.isfile(file_path):
            try:
                # Compress the file using gzip
                subprocess.run(['gzip', file_path], check=True)
                
                # Get the compressed file path
                compressed_file_path = file_path + '.gz'
                
                # Move the compressed file to the destination folder
                shutil.move(compressed_file_path, dst_folder)
            except subprocess.CalledProcessError:
                failed_files.append(os.path.basename(file_path))
            except Exception as e:
                failed_files.append(os.path.basename(file_path))
                print(f"An error occurred: {e}")

    # Determine if all files were processed successfully
    success = len(failed_files) == 0

    # Prepare the result message
    if success:
        message = "All files were compressed and moved successfully."
    else:
        message = f"Failed to compress or move the following files: {', '.join(failed_files)}"

    # Return the result as a dictionary
    return {
        'success': success,
        'message': message,
        'failed_files': failed_files
    }