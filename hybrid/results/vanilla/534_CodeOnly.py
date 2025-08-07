import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def task_func(num, from_base, to_base, private_key, alphabet):
    # Convert the number from the source base to base 10
    num_base10 = int(num, from_base)
    
    # Convert the number from base 10 to the target base
    if to_base == 10:
        num_base_to = str(num_base10)
    else:
        num_base_to = ''
        while num_base10 > 0:
            num_base_to = str(num_base10 % to_base) + num_base_to
            num_base10 //= to_base
    
    # Sign the number using the private RSA key
    signature = private_key.sign(
        num_base_to.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    # Encode the signed number in base64 using the custom alphabet
    # First, encode the signature in standard base64
    standard_base64 = base64.b64encode(signature).decode('utf-8')
    
    # Create a translation table from standard base64 to custom alphabet
    standard_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    translation_table = str.maketrans(standard_alphabet, alphabet)
    
    # Translate the standard base64 to custom base64
    custom_base64 = standard_base64.translate(translation_table)
    
    return custom_base64