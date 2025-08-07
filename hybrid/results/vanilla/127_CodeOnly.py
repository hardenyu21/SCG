import os
import shutil
import hashlib

def task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH):
    # Ensure the destination directory exists
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    # Initialize a counter for the number of files moved
    files_moved = 0

    # Iterate over all files in the root directory
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)

            # Calculate the MD5 hash of the file
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            # Check if the file's hash matches the specific hash
            if file_hash == SPECIFIC_HASH:
                # Construct the destination file path
                dest_file_path = os.path.join(DEST_DIR, file)

                # Move the file to the destination directory
                shutil.move(file_path, dest_file_path)

                # Increment the counter
                files_moved += 1

    # Return the number of files moved
    return files_moved