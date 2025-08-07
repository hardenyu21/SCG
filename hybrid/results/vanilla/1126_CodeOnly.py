import re
import hashlib

def task_func(input_str):
    # Remove all special characters, punctuation marks, and spaces
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)
    
    # Hash the cleaned string with SHA256
    sha256_hash = hashlib.sha256(cleaned_str.encode()).hexdigest()
    
    return sha256_hash