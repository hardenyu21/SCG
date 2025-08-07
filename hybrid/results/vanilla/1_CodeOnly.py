import collections
import random
import string

def task_func(length=100):
    if length < 0:
        raise ValueError("Length must be a non-negative number.")
    
    # Generate a random string of the specified length
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    
    # Count the occurrence of each character in the string
    char_count = collections.Counter(random_string)
    
    return dict(char_count)

# Example usage:
# result = task_func(100)
# print(result)