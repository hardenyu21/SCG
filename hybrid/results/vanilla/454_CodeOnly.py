import os
import shutil
import glob

def task_func(src_dir, dest_dir, ext):
    # Check if the source directory exists
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"The source directory '{src_dir}' does not exist.")
    
    # Check if the destination directory exists
    if not os.path.exists(dest_dir):
        raise FileNotFoundError(f"The destination directory '{dest_dir}' does not exist.")
    
    # Find all files with the specified extension in the source directory
    files_to_move = glob.glob(os.path.join(src_dir, f'*.{ext}'))
    
    # List to store the paths of successfully moved files
    moved_files = []
    
    # Iterate over the files found
    for file_path in files_to_move:
        file_name = os.path.basename(file_path)
        dest_file_path = os.path.join(dest_dir, file_name)
        
        # Check if the file already exists in the destination directory
        if not os.path.exists(dest_file_path):
            # Move the file
            shutil.move(file_path, dest_file_path)
            # Add the moved file path to the list
            moved_files.append(dest_file_path)
    
    return moved_files