import os
import hashlib

# Constants
DIRECTORY = "./hashed_files"

def task_func(input_string):
    # Ensure the directory exists
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    # Split the input string into lines
    lines = input_string.splitlines()
    
    # List to store file paths
    file_paths = []
    
    # Iterate over each line
    for line in lines:
        # Ignore empty lines
        if not line.strip():
            continue
        
        # Compute the SHA256 hash of the line
        sha256_hash = hashlib.sha256(line.encode()).hexdigest()
        
        # Create the filename using the first 10 characters of the hash
        filename = f"{sha256_hash[:10]}.txt"
        file_path = os.path.join(DIRECTORY, filename)
        
        # Write the hash to the file
        with open(file_path, 'w') as file:
            file.write(sha256_hash)
        
        # Add the file path to the list
        file_paths.append(file_path)
    
    # Return the list of file paths
    return file_paths