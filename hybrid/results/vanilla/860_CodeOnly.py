import re
import random
import string

def task_func(n, pattern, seed=None):
    # Set the seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Generate a random string of length 'n' using ASCII letters and digits
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    
    # Find all non-overlapping matches of the regex pattern
    matches = re.findall(pattern, random_string)
    
    return matches

# Example usage
print(task_func(1000, r'[1-9]{2}', seed=1))