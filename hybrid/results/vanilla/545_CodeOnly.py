import codecs
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS):
    # Randomly select a hex string from the list
    random_hex = random.choice(hex_keys)
    
    # Convert the hex string to an integer
    int_value = int(random_hex, 16)
    
    # Convert the integer to a float using struct
    float_value = struct.unpack('!f', struct.pack('!I', int_value))[0]
    
    # Encode the float as a UTF-8 string
    float_str = str(float_value)
    utf8_encoded = float_str.encode('utf-8')
    
    return utf8_encoded

# Example usage
result = task_func()
print(result)