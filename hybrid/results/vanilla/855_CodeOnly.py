import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    # Initialize a counter to keep track of character frequencies
    char_counter = collections.Counter()
    
    # Generate n random strings
    for _ in range(n_strings):
        # Generate a random string of the specified length
        random_string = ''.join(random.choice(VALID_CHARACTERS) for _ in range(string_length))
        # Update the counter with characters from the generated string
        char_counter.update(random_string)
    
    # Convert the counter to a dictionary and return
    return dict(char_counter)

# Example usage:
# result = task_func(10, 5)
# print(result)