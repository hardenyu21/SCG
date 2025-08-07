import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS, seed=42):
    # Set the random seed for deterministic random choices
    if seed is not None:
        random.seed(seed)
    
    # Select a random hexadecimal string key
    selected_key = random.choice(hex_keys)
    
    # Validate the selected key
    if not all(c in '0123456789ABCDEFabcdef' for c in selected_key):
        raise ValueError("Invalid hexadecimal string")
    
    # Convert the hexadecimal string to a floating-point number
    # Assuming the hexadecimal string represents a 32-bit unsigned integer
    int_value = int(selected_key, 16)
    # Convert the integer to a float using struct
    float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]
    
    # Compute the MD5 hash of the floating-point number
    float_bytes = struct.pack('!f', float_value)
    md5_hash = hashlib.md5(float_bytes).hexdigest()
    
    return md5_hash

# Example usage
print(task_func())