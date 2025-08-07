import random
import string
import hashlib
import time

def task_func(data_dict: dict, seed=0) -> dict:
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Step 1: Add a key "a" with a value of 1
    data_dict['a'] = 1
    
    # Step 2: Generate a random salt of length 5 using lowercase ASCII letters
    salt = ''.join(random.choices(string.ascii_lowercase, k=5))
    
    # Step 3: Hash each value with the generated salt
    for key, value in data_dict.items():
        # Convert value to string and concatenate with salt
        concatenated = str(value) + salt
        # Hash the concatenated string using SHA-256
        hashed_value = hashlib.sha256(concatenated.encode()).hexdigest()
        # Update the value in the dictionary with the hashed string
        data_dict[key] = hashed_value
    
    # Step 4: Add a 'timestamp' key with the current UNIX timestamp as its value
    data_dict['timestamp'] = int(time.time())
    
    return data_dict