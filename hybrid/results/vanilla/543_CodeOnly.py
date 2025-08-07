import base64
import os
import struct

def task_func():
    # Generate a random float number
    random_float = struct.unpack('!f', os.urandom(4))[0]
    
    # Convert the float to a hexadecimal string
    hex_representation = float.hex(random_float)
    
    # Encode the hexadecimal string in base64
    base64_encoded = base64.b64encode(hex_representation.encode('utf-8')).decode('utf-8')
    
    return base64_encoded

# Example usage
print(task_func())