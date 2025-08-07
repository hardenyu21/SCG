import hashlib
import os

def task_func(file_path1, file_path2):
    # Check if both files exist
    if not os.path.exists(file_path1):
        raise FileNotFoundError(f"The file {file_path1} does not exist.")
    if not os.path.exists(file_path2):
        raise FileNotFoundError(f"The file {file_path2} does not exist.")
    
    # Function to compute MD5 hash of a file
    def compute_md5(file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    # Compute MD5 hashes for both files
    md5_hash1 = compute_md5(file_path1)
    md5_hash2 = compute_md5(file_path2)
    
    # Compare the MD5 hashes
    return md5_hash1 == md5_hash2