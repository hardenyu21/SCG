import json
import hashlib
import blake3

def task_func(req_data):
    # Convert the request data to a JSON string
    json_data = json.dumps(req_data, sort_keys=True)
    
    # Hash the JSON string with BLAKE3
    blake3_hash = blake3.blake3(json_data.encode()).hexdigest()
    
    # Generate an MD5 hash of the BLAKE3 hash for demonstration purposes
    md5_hash = hashlib.md5(blake3_hash.encode()).hexdigest()
    
    # Return the BLAKE3 hash and the MD5 hash as a tuple
    return (blake3_hash, md5_hash)

# Example usage:
# req_data = {"key": "value", "number": 42}
# print(task_func(req_data))