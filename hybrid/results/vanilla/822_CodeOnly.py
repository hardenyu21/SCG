import random
import string

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):
    if num_digits > length:
        raise ValueError("Number of digits cannot be greater than the total length of the password.")
    
    # Generate the specified number of random digits
    digit_part = random.choices(DIGITS, k=num_digits)
    
    # Generate the remaining part of the password with random letters
    letter_part = random.choices(LETTERS, k=length - num_digits)
    
    # Combine both parts
    password_list = digit_part + letter_part
    
    # Shuffle the combined list to ensure randomness
    random.shuffle(password_list)
    
    # Join the list into a string and return
    return ''.join(password_list)

# Example usage:
# password = task_func(10, 3)
# print(password)