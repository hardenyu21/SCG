import struct
import random

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_key=None):
    # If no specific hex_key is provided, choose one randomly from KEYS
    if hex_key is None:
        hex_key = random.choice(KEYS)
    
    # Convert the hexadecimal string to a float
    # First, convert the hex string to bytes
    hex_bytes = bytes.fromhex(hex_key)
    
    # Unpack the bytes to a float using struct
    # Assuming the hex string represents a 32-bit float
    float_number = struct.unpack('!f', hex_bytes)[0]
    
    # Round the float number to 2 decimal places
    rounded_float = round(float_number, 2)
    
    return rounded_float

# Example usage
rounded_float = task_func()
print(rounded_float)