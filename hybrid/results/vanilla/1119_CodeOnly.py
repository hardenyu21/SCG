import codecs
import random
import string
import hashlib

def task_func(password_length=10, salt="salty"):
    # Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    # Mix the password with the salt
    salted_password = password + salt
    
    # Hash the salted password using SHA256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    
    return hashed_password

# Example usage:
# hashed = task_func(12, "my_salt")
# print(hashed)