import struct
import zlib

# Constants
KEY = '470FC614'

def task_func(hex_string=KEY):
    # Convert hex string to bytes
    hex_bytes = bytes.fromhex(hex_string)
    
    # Unpack bytes to a float
    float_number = struct.unpack('!f', hex_bytes)[0]
    
    # Pack the float back to bytes
    float_bytes = struct.pack('!f', float_number)
    
    # Compress the float bytes using zlib
    compressed_bytes = zlib.compress(float_bytes)
    
    return compressed_bytes

# Example usage
if __name__ == "__main__":
    compressed_float = task_func()
    print(compressed_float)