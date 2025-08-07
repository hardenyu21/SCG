import os
import shutil

def task_func(src_folder, backup_dir):
    try:
        # Check if the source folder exists
        if not os.path.exists(src_folder):
            raise ValueError(f"The source folder '{src_folder}' does not exist.")
        
        # Ensure the backup directory exists
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        # Define the backup path
        backup_path = os.path.join(backup_dir, os.path.basename(src_folder))
        
        # Backup the source folder to the backup directory
        shutil.copytree(src_folder, backup_path)
        
        # Delete the source folder
        shutil.rmtree(src_folder)
        
        return True
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False
    except Exception as e:
        print(f"An error occurred while deleting the source folder: {e}")
        return False