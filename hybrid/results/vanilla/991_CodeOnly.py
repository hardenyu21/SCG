import binascii
import string
import random

def task_func(length):
    # Generate a random hexadecimal string of the given length
    hex_string = ''.join(random.choices('0123456789abcdef', k=length))
    
    try:
        # Decode the hexadecimal string to ASCII
        ascii_string = binascii.unhexlify(hex_string).decode('ascii')
    except (binascii.Error, UnicodeDecodeError):
        # If decoding fails, return an empty string
        ascii_string = ''
    
    return ascii_string

# Example usage:
# print(task_func(10))