import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    def calculate_sha256(file_path: str) -> str:
        """Calculate the SHA256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    hashes = {}
    # Walk through all directories and files in the specified directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            hashes[relative_path] = calculate_sha256(file_path)

    # Define the path for the JSON file
    json_file_path = os.path.join(directory, 'hashes.json')
    
    # Write the hashes to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(hashes, json_file, indent=4)

    # Return the absolute path of the JSON file
    return os.path.abspath(json_file_path)