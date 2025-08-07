import os
import shutil

def task_func(src_dir, dest_dir, extension):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Initialize a counter for the number of files moved
    files_moved = 0

    # Iterate over all files in the source directory
    for filename in os.listdir(src_dir):
        # Check if the file has the specified extension
        if filename.endswith(extension):
            # Construct full file paths
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)

            # Move the file
            shutil.move(src_file, dest_file)
            files_moved += 1

    return files_moved