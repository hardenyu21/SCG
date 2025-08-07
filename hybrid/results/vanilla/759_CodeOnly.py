import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # List to store the names of files that were moved
    moved_files = []

    # Iterate over all files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the filename matches the pattern
        if fnmatch.fnmatch(filename, file_pattern):
            # Construct full file paths
            source_file = os.path.join(source_directory, filename)
            destination_file = os.path.join(destination_directory, filename)

            # Move the file
            shutil.move(source_file, destination_file)

            # Add the filename to the list of moved files
            moved_files.append(filename)

    # Return the list of moved files
    return moved_files