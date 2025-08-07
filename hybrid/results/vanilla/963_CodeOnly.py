import os
import glob
from pathlib import Path
import zipfile

def task_func(source_directory, target_directory, zip_name):
    # Define valid extensions
    valid_extensions = ['.txt', '.docx', '.xlsx', '.csv']
    
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise OSError(f"The source directory '{source_directory}' does not exist.")
    
    # Create the target directory if it does not exist
    os.makedirs(target_directory, exist_ok=True)
    
    # Construct the full path for the zip file
    zip_path = os.path.join(target_directory, f"{zip_name}.zip")
    
    # Create a zip file
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Iterate over each valid extension
        for ext in valid_extensions:
            # Find all files with the current extension in the source directory
            files = glob.glob(os.path.join(source_directory, f"*{ext}"))
            # Add each file to the zip file
            for file in files:
                zipf.write(file, os.path.basename(file))
    
    # Return the full path to the created zip file
    return zip_path