import string
import random

def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    
    def random_letter(c):
        if c.islower():
            return random.choice(string.ascii_lowercase)
        elif c.isupper():
            return random.choice(string.ascii_uppercase)
        else:
            return c
    
    transformed_text = ''.join(random_letter(c) for c in text)
    return transformed_text

# Example usage:
# print(task_func("Hello, World! 123", seed=42))