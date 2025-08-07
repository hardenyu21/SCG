import os
import pathlib
from hashlib import md5
import unicodedata

def task_func(directory):
    def normalize_filename(filename):
        # Normalize the filename to ASCII
        normalized = unicodedata.normalize('NFKD', filename)
        return ''.join(c for c in normalized if ord(c) < 128)

    def calculate_md5(file_path):
        # Calculate the MD5 hash of the file
        hash_md5 = md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    result = {}
    
    # Iterate over all files in the specified directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            normalized_name = normalize_filename(file)
            
            # Get the file size
            file_size = os.path.getsize(file_path)
            
            # Calculate the MD5 hash
            file_md5 = calculate_md5(file_path)
            
            # Store the results in the dictionary
            result[normalized_name] = {
                'Size': file_size,
                'MD5 Hash': file_md5
            }
    
    return result