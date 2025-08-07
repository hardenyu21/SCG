import json
import os
import hashlib
import base64
import time

def task_func(file_path, unknown_key):
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract the value to be hashed
    try:
        value_to_hash = data['A'][unknown_key]['maindata'][0]['Info']
    except KeyError as e:
        raise ValueError(f"Key error: {e}. The JSON structure does not match the expected format.")
    
    # Hash the value using SHA256
    sha256_hash = hashlib.sha256(value_to_hash.encode()).digest()
    
    # Encode the hash in base64
    base64_encoded_hash = base64.b64encode(sha256_hash).decode('utf-8')
    
    # Create a timestamped file name
    timestamp = int(time.time())
    new_file_name = f"hashed_value_{timestamp}.txt"
    
    # Write the base64-encoded hash to a new file
    new_file_path = os.path.abspath(new_file_name)
    with open(new_file_path, 'w') as new_file:
        new_file.write(base64_encoded_hash)
    
    # Return the absolute file path of the newly created file
    return new_file_path