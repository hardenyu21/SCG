import string
import random

BRACKETS = "(){}[]"

def task_func(length, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    # Create a pool of characters including lowercase letters and brackets
    char_pool = string.ascii_lowercase + BRACKETS
    
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(char_pool) for _ in range(length))
    
    return random_string

# Example usage:
string1 = task_func(34, random_seed=42)
print(string1)  # Output: hbrpoigf)cbfnobm(o{rak)vrjnvgfygww

string2 = task_func(23, random_seed=1)
print(string2)  # Output: ieqh]{[yng]by)a{rogubbb