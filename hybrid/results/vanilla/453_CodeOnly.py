import re
import string
from random import choice

def task_func(n, pattern):
    while True:
        # Generate a random string of length n using uppercase and lowercase letters
        random_string = ''.join(choice(string.ascii_letters) for _ in range(n))
        # Check if the generated string matches the given pattern
        if re.match(pattern, random_string):
            return random_string

# Example usage:
# This will generate a random string of length 3 that consists only of uppercase letters
print(task_func(3, '^[A-Z]+$'))