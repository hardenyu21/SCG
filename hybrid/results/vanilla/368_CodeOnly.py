import os
import shutil
import random

def task_func(src_dir: str, dest_dir: str, seed: int = 100) -> str:
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # List all files in the source directory
    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    
    # Check if there are any files to move
    if not files:
        raise FileNotFoundError("No files found in the source directory.")
    
    # Select a random file
    random_file = random.choice(files)
    
    # Construct full file paths
    src_file_path = os.path.join(src_dir, random_file)
    dest_file_path = os.path.join(dest_dir, random_file)
    
    # Move the file to the destination directory
    shutil.move(src_file_path, dest_file_path)
    
    # Return the name of the file moved
    return random_file