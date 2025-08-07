import os
import hashlib
import re

OUTPUT_DIR = './output'

def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    # Compile the regex pattern for matching
    regex = re.compile(pattern)
    
    # Dictionary to store file paths and their SHA256 hashes
    file_hashes = {}
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            
            # Check if the file path matches the regex pattern
            if regex.search(file_path):
                # Compute the SHA256 hash of the file's content
                sha256_hash = hashlib.sha256()
                try:
                    with open(file_path, 'rb') as f:
                        # Read and update hash string value in blocks of 4K
                        for byte_block in iter(lambda: f.read(4096), b""):
                            sha256_hash.update(byte_block)
                    # Store the hash in the dictionary
                    file_hashes[file_path] = sha256_hash.hexdigest()
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    return file_hashes