import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
    
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # List to store paths of newly created files
    new_files = []
    
    # Iterate over all files in the source directory
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        if os.path.isfile(file_path):
            # Read the content of the file
            with open(file_path, 'rb') as file:
                content = file.read()
            
            # Compute the MD5 hash of the file content
            md5_hash = hashlib.md5(content).hexdigest()
            
            # Create the new content with the hash prepended
            new_content = (prefix + md5_hash + '\n').encode() + content
            
            # Determine the target file path
            file_name = os.path.basename(file_path)
            target_file_path = os.path.join(target_dir, file_name)
            
            # Write the new content to the target file
            with open(target_file_path, 'wb') as target_file:
                target_file.write(new_content)
            
            # Add the path of the newly created file to the list
            new_files.append(target_file_path)
    
    return new_files